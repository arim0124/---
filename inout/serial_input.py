'''아두이노에서 값 받아오는 거
김유신 담당'''

import serial
import time

import serial
import time

#데이터를 읽어 문자로 정리
def get_temhumgas(ser):
  if ser.in_waiting>0:
    line = ser.readline().decode('utf-8').strip()
    
    values = line.split(',')
    if len(values) == 3:
      temperature = float(values[0])
      humidity = float(values[1])
      gas = int(values[2])
      return temperature, humidity, gas
    return None, None, None

if __name__ == "__main__" :
  #연결 포트 COM3, 1초동안 데이터 없으면 종료
  ser = serial.Serial('COM3', 9600, timeout = 1)

  #아두이노 리셋 기다리기
  time.sleep(2)

  while True :
    temhumgas = get_temhumgas(ser)
    if temhumgas != None:
      print(temhumgas)
    else:
      pass