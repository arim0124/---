'''메인 기능
성아림 담당'''
import config as c
from inout import serial_input as sin
from inout import serial_output as sou
from utils import weather as w
import time
from datetime import datetime as d 


def main() : 
    while True : 
        #센서 입력
        dust = sin.get_dust()
        tem, hum, gas = sin.get_temhumgas()
        if tem is None : 
            continue

        #무슨 동작할지 판단!
        now = d.now()
        hm = [now.hour, now.minute]
        if hm in c.PE_TIME : #체육시간 마치기 15분 전에 에어컨 튼다
            state = [True, False, False, False, True] #냉방, 난방, 제습, 송풍, 창문 닫기 순서
        else : #체육시간 아님
            if tem>c.HOT_TEMPERATURE : #더우면 에어컨
                state = [True, False, False, False, True]
            elif tem<=c.COLD_TEMPERATURE : #추우면 히터
                state = [False, True, False, False, True]
            else : #안덥고 안추움
                if dust>c.HIGH_DUST : #미세먼지!!
                    if gas>c.BAD_AIR : #근데 실내공기질 별로라 송풍
                        state = [False, False, False, True, True]
                    elif hum>c.WET : #근데 습해서 제습
                        state = [False, False, True, False, True]
                    else : #그냥 미세먼지 나쁘기만 함
                        state = [False, False, False, False, True]
                else : #미세먼지 없으요
                    if gas>c.BAD_AIR or hum>c.WET: #실내 공기 탁하거나 습해서 창문 열기
                        state = [False, False, False, False, False]
                    else : 
                        state = [False, False, False, False, True] #아무것도 아니라 창문 닫음


        #자 행동하세요 라고 명령
        cac, hac, js, sp, wd = state
        if cac : 
            sou.con_aircon()
        elif hac : 
            sou.hon_aircon()
        elif js : 
            sou.js_aircon()
        elif sp : 
            sou.sp_aircon()
        else : 
            sou.off_aircon()

        if wd : 
            sou.close_window()
        else : 
            sou.open_window()


        #2초 주기로 ㄱㄱ
        time.sleep(2)




if __name__ == "__main__" : 
    main()