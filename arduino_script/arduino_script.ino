#include <LiquidCrystal.h>


const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

void setup() {
  lcd.begin(16, 2);
  Serial.begin(9600);

}

void loop() {
  if (Serial.available()) {
    String message = Serial.readStringUntil('\n');
    lcd.clear();
    lcd.print(message);
    Serial.println(message);
  }
}
