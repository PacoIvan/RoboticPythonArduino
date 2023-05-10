int estado;
int M1A=2;
int M1B=3;
int M2A=4;
int M2B=5;
void setup() {
// put your setup code here, to run once:
//motor izq
pinMode(M1A, OUTPUT);
pinMode(M1B, OUTPUT);
//motor derecho
pinMode(M2A, OUTPUT);
pinMode(M2B, OUTPUT);
Serial.begin(9600);
}
void loop()
{
if(Serial.available()>0)
{
estado=Serial.read();
}
if(estado=='A'){
// Serial.println("a");
adelante();
}
if(estado=='B'){
izquierda();
}
if(estado=='C'){
derecha();
}
if(estado=='D'){
atras();
}
if(estado=='E'){
detener();
}
}
void adelante(){
digitalWrite(M1A, HIGH);
digitalWrite(M1B, LOW);
digitalWrite(M2A, HIGH);
digitalWrite(M2B, LOW);
}
void izquierda(){
digitalWrite(M1A, LOW);
digitalWrite(M1B, HIGH);
digitalWrite(M2A, HIGH);
digitalWrite(M2B, LOW);
}
void derecha(){
digitalWrite(M1A, HIGH);
digitalWrite(M1B, LOW);
digitalWrite(M2A, LOW);
digitalWrite(M2B, HIGH);
}
void atras(){
digitalWrite(M1A, LOW);
digitalWrite(M1B, HIGH);
digitalWrite(M2A, LOW);
digitalWrite(M2B, HIGH);
}
void detener(){
digitalWrite(M1A, LOW);
digitalWrite(M1B, LOW);
digitalWrite(M2A, LOW);
digitalWrite(M2B, LOW);
}
