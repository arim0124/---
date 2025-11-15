'''출력값 보내는 코드
정재균 담당'''

import serial
import time

#각 기능별 함수 - 회로 연결시 버그 없었음
#각 함수당 ser이 아두이노랑 연결하는 객체인데 이걸 메인에서 연결해서 전달하면됨 - 예제는 대충 얘네거 참고해서 하시고
def open_window(ser):
    ser.write('WIN_ON\n'.encode('utf-8'))

def close_window(ser):
    ser.write('WIN_OFF\n'.encode('utf-8'))

def sp_aircon(ser):
    ser.write('FAN\n'.encode('utf-8'))

def js_aircon(ser):
    ser.write('DRY\n'.encode('utf-8'))

def hon_aircon(ser):
    ser.write('HEAT\n'.encode('utf-8'))

def con_aircon(ser):
    ser.write('COOL\n'.encode('utf-8'))

def off_aircon(ser):
    ser.write('OFF\n'.encode('utf-8'))

if __name__ == "__main__" :
  #연결 포트 COM3, 1초동안 데이터 없으면 종료
  ser = serial.Serial('COM3', 9600, timeout = 1)

  #아두이노 리셋 기다리기
  time.sleep(2)

  open_window(ser)
  time.sleep(1)
  close_window(ser)
  time.sleep(1)
  sp_aircon(ser)
  time.sleep(1)
  js_aircon(ser)
  time.sleep(1)
  off_aircon(ser)
  time.sleep(1)
  con_aircon(ser)
  time.sleep(1)
  hon_aircon(ser)