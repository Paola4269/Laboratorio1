const int ledA = 2;
const int ledV = 4;
const int ledR = 6;
void setup(){
  pinMode(ledA, OUTPUT);
  pinMode(ledV, OUTPUT);
  pinMode(ledR, OUTPUT);
}

void loop(){
  digitalWrite(ledA, HIGH);
  delay(1000);
  digitalWrite(ledA, LOW);

  digitalWrite(ledV, HIGH);
  delay(1000);
  digitalWrite(ledV, LOW);
  
  digitalWrite(ledR, HIGH);
  delay(1000);
  digitalWrite(ledR, LOW);
}
