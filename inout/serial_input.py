'''아두이노에서 값 받아오는 거
김유신 담당'''

def get_temhumgas(ser):
  if ser.in_waiting>0:
    line = ser.readline().decode('utf-8').strip()
    
    values = line.split(',')
    if len(values) == 3:
      temperature = float(values[0])
      humidity = float(values[1])
      gas = int(values[2])
      return temperature, humidity, gas
    return (None, None, None)