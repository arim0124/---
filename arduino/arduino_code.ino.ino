#include <Servo.h>
#include <DHT.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>
// 모듈 불러오기

#define DHTPIN 2     
#define DHTTYPE DHT11
#define GAS_PIN A3
#define SERVO_PIN 3
// 각 연결 핀 정의

DHT dht(DHTPIN, DHTTYPE);
Servo servo;
LiquidCrystal_I2C lcd(0x27, 16, 2); 
// 객체 생성 - 온습도, 서보, 디스플레이 (디스플레이는 주소 설정 - 0x27 0x3F 둘중하나)

void setup() {
  dht.begin(); 
  servo.attach(SERVO_PIN);
  lcd.init();
  lcd.backlight();
  lcd.setCursor(0, 0);
  delay(2000); // 셋업시 걸리는 시간 (안정화에 따라 변동 가능)
}
// 초기 세팅 - 온습도, 서보연결, 디스플레이 키고, 불키고, 커서 세팅

void loop() {
  delay(2000);  // 2초 새로고침

  float h = dht.readHumidity();    
  float t = dht.readTemperature();
  int g = analogRead(GAS_PIN);
  // 입력 받기 습도,온도,가스

  if (isnan(h) || isnan(t)) {
    Serial.println("NaN");  
  } else {
    Serial.print(t); Serial.print(",");
    Serial.print(h); Serial.print(",");
    Serial.println(g);
  }
  // 습도,온도,가스 출력 - (없으면 nan 출력, 있으면 (온도,습도,가스) 형태로 출력)

  if (Serial.available()){
    String cmd =
    Serial.readStringUntil('\n');
    cmd.trim();
    // 입력받아서 \n 까지 입력 받기 , 앞뒤 공백 제외

    while (cmd.length() > 0) {
      int commaIndex = cmd.indexOf(',');
      String part;
      // 입력값의 첫번쨰 콤마 위치 반환 - (없으면 -1 반환)
      // part 부분 변수 생성

      if (commaIndex != -1) {
        part = cmd.substring(0,commaIndex);
        cmd = cmd.substring(commaIndex+1);
      }
      else {
        part = cmd;
        cmd= "";
      }
      part.trim();
      // 0부터 콤마 전까지를 명령으로 part에 추출 , 그리고 cmd에서 제외, 그리고 앞뒤 공백 제외

      if (part == "WIN_ON") {
        servo.write(0);
      }
      else if (part == "WIN_OFF") {
        servo.write(90);
      }
      else if (part == "COOL") {
        lcd.setCursor(0, 0);
        lcd.print("COOL                ");
      }
      else if (part == "HEAT") {
        lcd.setCursor(0, 0);
        lcd.print("HEAT                ");
      }
      else if (part == "FAN") {
        lcd.setCursor(0, 0);
        lcd.print("FAN                ");
      }
      else if (part == "DRY") {
        lcd.setCursor(0, 0);
        lcd.print("DRY                ");
      }
      else if (part == "OFF") {
        lcd.setCursor(0, 0);
        lcd.print("OFF                ");
      }
      // 명령 실행 - ( 처음 둘은 창문 , 뒤 다섯은 에어컨 , 빈칸은 글자 초기화 )
    }
  }
}