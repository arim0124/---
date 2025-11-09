'''메인 기능
성아림 담당'''
import config as c
from serial import serial_input as sin
from serial import serial_output as sou
from utils import weather as w
import multiprocessing as m
import time
from datetime import datetime as d 

def sensor(q) : 
    while True : 
        dust = sin.get_dust()
        tem, hum = sin.get_temhum()
        gas = sin.get_gas()

        data = [dust, tem, hum, gas]
        q.put(data)
        time.sleep(1)


def judging(a, b) : 
    while True : 
        data = a.get()
        dust, tem, hum, gas = data
        now = datetime.now()
        hm = [now.hour, now.minute]
        if hm == c.PE_TIME[0] or hm == c.PE_TIME[1] : 
            state = [True, True, False] #냉방, 창문 닫기, 제습 순서

            

def act() : 
    while True : 


if __name__ == "__main__" : 
    q1 = m.Queue()
    q2 = m.Queue()

    p1 = m.Process(target=sensor, args = (q1,))
    p2 = m.Process(target=judging, args = (q1,q2))
    p3 = m.Process(target=act, args = (q2))

    p1.start()
    p2.start()
    p3.start()