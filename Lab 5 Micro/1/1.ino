int potenciometro1;
int potenciometro2;
int potenciometro3;
String pot;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600); 
  potenciometro1=-1;
  potenciometro2=-1;
  potenciometro3=-1;
}

void loop() {
  
  if (analogRead(A0)!=potenciometro1 || analogRead(A1)!=potenciometro2 || analogRead(A2)!=potenciometro3){
    potenciometro1 = analogRead(A0);
    potenciometro2 = analogRead(A1);
    potenciometro3 = analogRead(A2);
    pot=String(potenciometro1)+','+String(potenciometro2)+','+String(potenciometro3)+',';
    Serial.println(pot);
}
  

}
