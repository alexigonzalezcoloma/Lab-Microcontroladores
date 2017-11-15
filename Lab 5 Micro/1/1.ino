int potenciometro1;
int potenciometro2;
int potenciometro3;
int potenciometro4;
String pot;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600); 
}

void loop() {
  potenciometro1 = analogRead(A0);
  potenciometro2 = analogRead(A1);
  potenciometro3 = analogRead(A2);
  potenciometro4 = analogRead(A3);
  if (analogRead(A0)!=potenciometro1 || analogRead(A1)!=potenciometro2 || analogRead(A2)!=potenciometro3 || analogRead(A3)!=potenciometro4){
    int p1=map(potenciometro1,0,1023,0,360);
    int p2=map(potenciometro2,0,1023,0,360);
    int p3=map(potenciometro3,0,1023,0,360);
    int p4=map(potenciometro4,0,1023,0,360);

    pot=String(p1)+","+String(p2)+","+String(p3)+","+String(p4);
    Serial.println(pot);
    
  }
 
