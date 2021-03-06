#!/usr/bin/env python3
# -*- coding: utf-8 -*-

IP = "192.168.42.10"
PORT = 8000

SEND_DELAY = 0.25  # время задержки отправки новых данных

TURN_STICK = 'x'  # имя поворотного стика(передняя часть робота)
TURN_ALL_STICK = 'hat0x'
ROTATE_STICK = 'hat0x'  # имя стика разворота на месте
MOVE_STICK = 'hat0y'  # имя стика движения робота
SPEED_CHANGE_STEP = 10  # размер шага изменения максимальной, при прибавлении или уменьшении с кнопки
ADD_SPEED_BUTTON = 'pinkie'  # имя кнопки прибавления скорости
SUB_SPEED_BUTTON = 'base2'  # имя кнопки уменьшениия скорости
SET_AUTO_BUTTON = 'base3'    # имя кнопки установки автономки
ROTATE_CAMERA_BUTTON = 'base4'   # имя кнопки поворота камеры
SET_MANIPULATOR_HOME = 'base' # Установка манипулятора в сложенное состояние
SET_MANIPULATOR_WORK = 'top2' # Установка манипулятора в сложенное состояние


TURN_FIRST_DOF = 'z' # имя стика поворота основания манипулятора влево
TURN_SECOND_DOF = 'rz' # имя стика поворота второй степени манипулятора
TURN_UP_THIRD_DOF = 'top' # имя кнопки движения третьей степени манипулятора вверх
TURN_DOWN_THIRD_DOF = 'thumb' # имя кнопки движения третьей степени манипулятора вниз
TURN_LEFT_FOURTH_DOF = 'trigger' # имя кнопки сжатия схвата манипулятора
TURN_RIGHT_FOURTH_DOF = 'thumb2' # имя кнопки разжатия схвата манипулятора
