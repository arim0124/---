'''메인 기능
성아림 담당'''
from inout import serial_input as sin
from inout import serial_output as sou
from utils import weather as w
from utils import create_button,root
import time
from datetime import datetime as d 
import serial
import threading
import queue

cmd_queue = queue.Queue()

def main(ser) : 
    while True : 
        try:
            cmd = cmd_queue.get_nowait()
            time.sleep(60)
        except queue.Empty:
            #센서 입력
            dust = int(w.get_dust())
            temhumgas = sin.get_temhumgas(ser)
            if temhumgas is None : 
                continue
            tem = temhumgas[0]
            hum = temhumgas[1]
            gas = temhumgas[2]

            #무슨 동작할지 판단!
            now = d.now()
            hm = [now.hour, now.minute]
            print([hm,tem,hum,gas,dust])
            sou.act(ser,[hm,tem,hum,gas,dust])

            #2초 주기로 ㄱㄱ
            time.sleep(2)

ser = serial.Serial('COM3', 9600, timeout = 1)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

create_button(50, 50, screen_width//2 - 25, 150, "창문 열기", lambda: sou.direct_act(ser,cmd_queue,'WIN_ON\n'))
create_button(screen_width//2 + 25, 50, screen_width - 50, 150, "창문 닫기", lambda: sou.direct_act(ser,cmd_queue,'WIN_OFF\n'))

x1_right = screen_width*2//3
y1_right = 200
x2_right = screen_width - 50
y2_right = screen_height - 50
create_button(x1_right, y1_right, x2_right, y2_right, "에어컨 끄기", lambda: sou.direct_act(ser,cmd_queue,'OFF\n'))

left_w = screen_width*2//3 - 60
left_h = y2_right - y1_right
btn_w = (left_w - 30)//2
btn_h = (left_h - 30)//2
ln = [['냉방','난방'],['제습','송풍']]
lc = [['COOL\n','HEAT\n'],['DRY\n','FAN\n']]
for i in range(2):
    for j in range(2):
        x1 = 50 + j*(btn_w + 10)
        y1 = y1_right + i*(btn_h + 10)
        x2 = x1 + btn_w
        y2 = y1 + btn_h
        create_button(x1, y1, x2, y2, ln[i][j], lambda i=i, j=j : sou.direct_act(ser,cmd_queue,lc[i][j]) )
time.sleep(2)
    
thread = threading.Thread(target=main,args=(ser,),daemon=True)
thread.start()
    
root.mainloop()