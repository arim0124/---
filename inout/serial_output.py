'''출력값 보내는 코드
정재균 담당'''
import serial
import time

ser=serial.Serial('COM3',9600,timeout=1)

time.sleep(2)

def open_window():
    ser.write('WIN_ON\n')

def close_window():
    ser.write('WIN_OFF\n')

def sp_aircon():
    ser.write('FAN\n')

def js_aircon():
    ser.write('DRY\n')

def hon_aircon():
    ser.write('HEAT\n')

def con_aircon():
    ser.write('COOL\n')

def off_aircon():
    ser.write('OFF\n')