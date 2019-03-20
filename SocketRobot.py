#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sender

SPEED_FIRST_DOF = 3.0
SPEED_SECOND_DOF = 3.0
SPEED_THIRD_DOF = 3.0
SPEED_FOURTH_DOF = 3.0

MAX_FIRST_DOF = 90.0
MIN_FIRST_DOF = -90.0

MAX_SECOND_DOF = 92.0
MIN_SECOND_DOF = -90.0

MAX_THIRD_DOF = 100.0
MIN_THIRD_DOF = -100.0

MAX_FOURTH_DOF = 81.0
MIN_FOURTH_DOF = -69.0


class SocketRobot:
    def __init__(self):
        self._ip = None
        self._port = None
        self._sender = None
        self._motorSpeed = 0
        self._first_DOF = 0.0
        self._second_DOF = 0.0
        self._third_DOF = 0.0
        self._fourth_DOF = 0.0

        self._argDict = {
            "turnForwardArg": float(0.0),
            "moveArg": int(0.0),
            "rotateArg": int(0.0),
#            "turnAllArg": float(0.0),
            "setAutoArg": False,
            "setCameraArg": float(0.0),
            "turnFirstDOF": float(0.0),
            "turnSecondDOF": float(0.0),
            "turnThirdDOF": float(0.0),
            "turnFourthDOF": float(0.0)
        }

    def connect(self, ip, port):
        self._sender = sender.Sender(ip, port)
        self._sender.packageFormat = "fii?fffff"
        self._sender.connect()

    def _sendPackage(self):
        self._sender.sendPackage(self._sender.pack(
            self._argDict["turnForwardArg"], self._argDict["moveArg"],
            self._argDict["rotateArg"],
#            self._argDict["turnAllArg"],
            self._argDict["setAutoArg"], self._argDict["setCameraArg"],
            self._argDict["turnFirstDOF"], self._argDict["turnSecondDOF"],
            self._argDict["turnThirdDOF"], self._argDict["turnFourthDOF"]
        ))

    def turnForward(self, scale):  # scale - значение из диапазона (-1, 1)
        # поворачиваем сервами в зависимости от значения со стика
        self._argDict["turnForwardArg"] = float(scale)
        self._sendPackage()

    def move(self, scale):  # scale - значение из диапазона (-1, 1) # движемся вперед со скоростью
        # MotorSpeed*коэффициент scale
        self._argDict["moveArg"] = int(scale * self._motorSpeed)
        self._sendPackage()

    def rotate(self, scale):  # scale - значение из диапазона (-1, 1) # поворачиваемся со скоростью моторов
        # MotorSpeed*коэффициент scale
        self._argDict["rotateArg"] = int(scale * self._motorSpeed)
        self._sendPackage()

#    def turnAll(self, scale):  # поворачивает всеми сервами на один и тот же угол
#        self._argDict["turnAllArg"] = float(scale)
#        self._sendPackage()

    def setAuto(self, b):
        self._argDict["setAutoArg"] = bool(b)
        self._sendPackage()

    def setCamera(self, scale):
        self._argDict["setCameraArg"] = float(scale)
        self._sendPackage()

    def turnFirstDOF(self, scale):
        self.turnFirstDOFAngle += SPEED_FIRST_DOF * float(scale)
        self._argDict["turnFirstDOF"] = self.turnFirstDOFAngle
        self._sendPackage()

    def turnSecondDOF(self, scale):
        self.turnSecondDOFAngle += SPEED_SECOND_DOF * float(scale)
        self._argDict["turnSecondDOF"] = self.turnSecondDOFAngle
        self._sendPackage()

    def turnThirdDOF(self, scale):
        self.turnThirdDOFAngle += SPEED_THIRD_DOF * float(scale)
        self._argDict["turnThirdDOF"] = self.turnThirdDOFAngle
        self._sendPackage()

    def turnFourthDOF(self, scale):
        self.turnFourthDOFAngle += SPEED_FOURTH_DOF * float(scale)
        self._argDict["turnFourthDOF"] = self.turnFourthDOFAngle
        self._sendPackage()

    @property
    def online(self):  # создан ли клиент
        return bool(self._sender)

    @property
    def motorSpeed(self):
        return self._motorSpeed

    @motorSpeed.setter
    def motorSpeed(self, value):  # устанавливаем максимально возможную скорость движения, которая дальше будет
        #  изменяться в некотором диапазоне
        if value >= 100:
            self._motorSpeed = 100
        elif value <= - 100:
            self._motorSpeed = -100
        else:
            self._motorSpeed = value

    @property
    def turnFirstDOFAngle(self):
        return self._first_DOF

    @turnFirstDOFAngle.setter
    def turnFirstDOFAngle(self, value):  # устанавливаем максимально возможную скорость движения, которая дальше будет
        #  изменяться в некотором диапазоне
        if value >= MAX_FIRST_DOF:
            self._first_DOF = MAX_FIRST_DOF
        elif value <= MIN_FIRST_DOF:
            self._first_DOF = MIN_FIRST_DOF
        else:
            self._first_DOF = value

    @property
    def turnSecondDOFAngle(self):
        return self._second_DOF

    @turnSecondDOFAngle.setter
    def turnSecondDOFAngle(self, value):  # устанавливаем максимально возможную скорость движения, которая дальше будет
        #  изменяться в некотором диапазоне
        if value >= MAX_SECOND_DOF:
            self._second_DOF = MAX_SECOND_DOF
        elif value <= MIN_SECOND_DOF:
            self._second_DOF = MIN_SECOND_DOF
        else:
            self._second_DOF = value

    @property
    def turnThirdDOFAngle(self):
        return self._third_DOF

    @turnThirdDOFAngle.setter
    def turnThirdDOFAngle(self, value):  # устанавливаем максимально возможную скорость движения, которая дальше будет
        #  изменяться в некотором диапазоне
        if value >= MAX_THIRD_DOF:
            self._third_DOF = MAX_THIRD_DOF
        elif value <= MIN_THIRD_DOF:
            self._third_DOF = MIN_THIRD_DOF
        else:
            self._third_DOF = value

    @property
    def turnFourthDOFAngle(self):
        return self._fourth_DOF

    @turnFourthDOFAngle.setter
    def turnFourthDOFAngle(self, value):  # устанавливаем максимально возможную скорость движения, которая дальше будет
        #  изменяться в некотором диапазоне
        if value >= MAX_FOURTH_DOF:
            self._fourth_DOF = MAX_FOURTH_DOF
        elif value <= MIN_FOURTH_DOF:
            self._fourth_DOF = MIN_FOURTH_DOF
        else:
            self._fourth_DOF = value
