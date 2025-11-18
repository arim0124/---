'''기준값이랑 함수 이름. 필요한 것들 추가 ㄱㄱ

함수 이름들
get_dust() : 미세먼지 불러오기
get_temhumgas() : 온습도, 가스 불러오기
close_window : 창문 닫기
open_window() : 창문 열기
con_aircon() : 에어컨 냉방
hon_aircon() : 에어컨 난방
sp_aircon() : 에어컨 송풍
js_aircon() : 에어컨 제습
off_aircon() : 에어컨 끄기'''

HOT_TEMPERATURE = 30
COLD_TEMPERATURE = 18
WET = 50
BAD_AIR = 100 
HIGH_DUST = 400
PE_TIME = [
    [10, 15], [15, 15]
]

def whatcommand(time,tem,hum,gas,dust):
    if dust <= HIGH_DUST and (hum > WET or gas > BAD_AIR):
        command_1 = 'WIN_ON'
    else:
        command_1 = 'WIN_OFF'
    if time in PE_TIME or tem > HOT_TEMPERATURE:
        command_2 = 'COOL'
    elif tem < COLD_TEMPERATURE:
        command_2 = 'HEAT'
    elif dust > HIGH_DUST and hum > WET:
        command_2 = 'DRY'
    elif dust > HIGH_DUST and gas > BAD_AIR:
        command_2 = 'FAN'
    else:
        command_2 = 'OFF'
    
    return command_1,command_2