'''출력값 보내는 코드
정재균 담당'''
import sys,os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from config import whatcommand

def act(ser,state):
    
    c1,c2 = whatcommand(state[0],state[1],state[2],state[3],state[4])
    command = f"{c1},{c2}\n"
    ser.write(command.encode('utf-8'))

def direct_act(ser,cmd_queue,command):
    cmd_queue.put("pause_task")
    ser.write(command.encode('utf-8'))