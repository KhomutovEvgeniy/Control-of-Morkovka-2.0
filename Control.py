""" Модуль описывающий управление роботом """
import Robot
import threading
import time
from config import *
import SocketRobot


class Control(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self, daemon=True)
        self.robot = SocketRobot.SocketRobot()
        self._joystick = None
        self._auto = False
        self._cameraPos = False     # позиция камеры
        self._EXIT = False


    def setJoystick(self, joystick):  # устанавливаем джойстик, которым будем управлять
        self._joystick = joystick
        self.connectHandlers()

    def run(self):
        while not self._EXIT:
            try:
                if self.robot.online and (self._joystick is not None):  # если клиент и джойстик созданы
                    if int(self._joystick.Axis.get(ROTATE_STICK)*100.0) == 0:  # если нет разворота на месте в
                        # приближении(некоторые стики повреждены))
                        self.robot.rotate(0.0)  # убираем поворот
                        self.robot.turnForward(self._joystick.Axis.get(TURN_STICK))  # поворот
                        self.robot.move(self._joystick.Axis.get(MOVE_STICK))  # движение

                        # поворот основания манипулятора - в какую сторону отклоняется стик - в ту сторону поворот
                        self.robot.turnFirstDOF(self._joystick.Axis.get(TURN_FIRST_DOF))

                        # поворот второй степенью манипулятора - в какую сторону отклоняется стик - в ту сторону поворот
                        self.robot.turnSecondDOF(self._joystick.Axis.get(TURN_SECOND_DOF))

                        # поворот третьей степени манипулятора - жмешь кнопку - поворачивает
                        self.robot.turnThirdDOF(self._joystick.Buttons.get(TURN_DOWN_THIRD_DOF)
                                                - self._joystick.Buttons.get(TURN_UP_THIRD_DOF))

                        # схват манипулятора - жмешь кнопку - поворачивает)
                        self.robot.turnFourthDOF(self._joystick.Buttons.get(TURN_LEFT_FOURTH_DOF)
                                                - self._joystick.Buttons.get(TURN_RIGHT_FOURTH_DOF))

                    else:
                        self.robot.rotate(self._joystick.Axis.get(ROTATE_STICK))     # поворот на месте
            except:
                print("Ошибка управления")

            time.sleep(SEND_DELAY)

    def connectHandlers(self):  # привязка обработчиков кнопок
        def addSpeed(w):
            if w:
                self.robot.motorSpeed += SPEED_CHANGE_STEP     # прибавляем скорость

        def subSpeed(w):
            if w:
                self.robot.motorSpeed -= SPEED_CHANGE_STEP     # уменьшаем скорость

        def setAutoButton(w):       # установка автономности
            if w:
                self._auto = not self._auto
                self.robot.setAuto(self._auto)

        def rotateCamera(w):
            if w:
                self._cameraPos = not self._cameraPos
                self.robot.setCamera(int(self._cameraPos))  # True - 1, False - 0


        self._joystick.connectButton(ADD_SPEED_BUTTON, addSpeed)
        self._joystick.connectButton(SUB_SPEED_BUTTON, subSpeed)
        self._joystick.connectButton(SET_AUTO_BUTTON, setAutoButton)
        self._joystick.connectButton(ROTATE_CAMERA_BUTTON, rotateCamera)

    def exit(self):
        self._EXIT = True
