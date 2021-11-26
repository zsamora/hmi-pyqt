#include <SoftwareSerial.h>   // Incluimos la librería  SoftwareSerial  
SoftwareSerial BT(10,11);     // Definimos los pines RX y TX del Arduino conectados al Bluetooth
char inputByte;
unsigned long previousMillis = 0;       
unsigned long interval = 1000;
byte ledState = LOW;
byte sequenceState = LOW;

void setup() {
  delay(1000);
  Serial.begin(9600);   // Inicializamos  el puerto serie    
  pinMode(13, OUTPUT);  // LED interno Arduino
  Serial.println("Esperando comandos AT...");
  BT.begin(9600);       // Inicializamos el puerto serie BT (Para Modo AT 2)
}
 
void loop() {
  unsigned long currentMillis = millis();
  if (BT.available()) { 
    inputByte = BT.read();
    Serial.print("Comando recibido: ");
    Serial.write(inputByte);
    Serial.println();
    if (inputByte=='O')
      sequenceState = HIGH;
    else if (inputByte=='X')
      sequenceState = LOW;
    else
      interval = 1000 / (inputByte - '0');
  }
  if (currentMillis - previousMillis >= interval) {
    previousMillis = currentMillis;
    if (ledState == LOW && sequenceState == HIGH)
      ledState = HIGH;
    else
      ledState = LOW;
    digitalWrite(13, ledState);
  }
}
