basic.show_icon(IconNames.HEART)

def on_forever():
    if Tinybit.Line_Sensor(Tinybit.enPos.LEFT_STATE, Tinybit.enLineState.WHITE) and Tinybit.Line_Sensor(Tinybit.enPos.RIGHT_STATE, Tinybit.enLineState.WHITE):
        Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_RUN, 70)
    elif Tinybit.Line_Sensor(Tinybit.enPos.LEFT_STATE, Tinybit.enLineState.BLACK) and Tinybit.Line_Sensor(Tinybit.enPos.RIGHT_STATE, Tinybit.enLineState.WHITE):
        Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_SPINLEFT, 70)
    elif Tinybit.Line_Sensor(Tinybit.enPos.LEFT_STATE, Tinybit.enLineState.WHITE) and Tinybit.Line_Sensor(Tinybit.enPos.RIGHT_STATE, Tinybit.enLineState.BLACK):
        Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_SPINRIGHT, 70)
    else:
        Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_STOP, 0)
basic.forever(on_forever)
