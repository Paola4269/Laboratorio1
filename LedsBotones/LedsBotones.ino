const int ledA = 2;
const int ledV = 4;
const int ledR = 6;
void setup() {
  pinMode(2, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if(Serial.available()>0){
    char estado = Serial.read();
    if(estado =='a'){
      digitalWrite(2, HIGH);
      digitalWrite(4, HIGH);
      digitalWrite(6, HIGH);
    }else if(estado =='b'){
      digitalWrite(2, LOW);
      digitalWrite(4, LOW);
      digitalWrite(6, LOW);
      //Serial.println("LED apagado");
    }else if(estado == 'c'){
      digitalWrite(2, HIGH);
    }else if(estado == 'd'){
      digitalWrite(2, LOW);
    }else if(estado == 'f'){
      digitalWrite(4, HIGH);
    }else if(estado == 'g'){
      digitalWrite(4, LOW);
    }else if(estado == 'h'){
      digitalWrite(6, HIGH);
    }else if(estado == 'i'){
      digitalWrite(6, LOW);
    }
  }
}
