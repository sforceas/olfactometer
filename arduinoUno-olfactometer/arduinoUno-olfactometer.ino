#include <Servo.h> // Se importa la libreria Servo

// Creación de objetos Servo

 Servo servoA;  // Crea un objeto "Servo" para el canal A
 Servo servoB;  // Crea un objeto "Servo" para el canal B
 Servo servoC;  // Crea un objeto "Servo" para el canal C
 Servo servoD;  // Crea un objeto "Servo" para el canal D (limpieza)

 pinServoA = 4;
 pinServoB = 5;
 pinServoC = 6;
 pinServoD = 7;

// Configuración de pines para L298N

 const int pinENA = 8 // Pin ENA del driver L298N
 const int pinIN1 = 9;
 const int pinIN2 = 10;
 const int speed = 200;    //velocidad de giro 80% (200/255)

// Configuración de pines para interfaz de botones

const int button1 = 2;
const int button2 = 12;
const int button3 = 13;

//Se crean las variables globales del test

int degreesClose = 25; //Grados del servomotor para cerrar el canal
int degreesOpen = 0; //Grados del servomotor para abrir el canal
int incomingByte ; // Numero Entero introducido en monitor serial


//Se crean las variables individuales del test

int t0 = 0;
int t1 = 0;
int t2 = 0;
int t3 = 0;
int t4 = 0;

float tResp = 0.0;
float tFinal = 0.0;






//Configuración inicial del microcontrolador
void setup() {
    
    servoA.attach(pinServoA);  // Asigna el pin Digital 3 al servo del canal A-1
    servoB.attach(pinServoB);  // Asigna el pin Digital 4 al servo del canal B-2
    servoC.attach(pinServoC);  // Asigna el pin Digital 5 al servo del canal C-3
    servoD.attach(pinServoD);  // Asigna el pin Digital 6 al servo del canal D-4

    //Cierra todos los canales
    servoA.write(degreesClose);
    servoB.write(degreesClose);
    servoC.write(degreesClose);
    servoD.write(degreesClose);
    
    //Configuración de pines del driver L298N
    pinMode(pinIN1, OUTPUT);
    pinMode(pinIN2, OUTPUT);
    pinMode(pinENA, OUTPUT);

    //Configuración de pines de interfaz de botones
    pinMode(button1, INPUT);
    pinMode(button2, INPUT);
    pinMode(button3, INPUT);
    pinMode(pin5v, OUTPUT);
    pinMode(pinGND, INPUT);

    Serial.begin(9600); // Inicia comunicación serial a una tasa de refresco de 9600 bps

    delay(100);    
    Serial.println("Indique el canal del test: 1, 2, 3 o 4.");

}


void loop() {


}



// Función para encender la bomba de aire
void startFlow(){
  digitalWrite(pinIN1, HIGH);
  digitalWrite(pinIN2, LOW);
  analogWrite(pinENA, speed);
  }

// Función para apagar la bomba de aire
void stopFlow(){
  digitalWrite(pinIN1, LOW);
  digitalWrite(pinIN2, LOW);
  analogWrite(pinENA, speed);
  }

//Funcion para abrir el canal (servomotor) indicado.
int channelOpen (int channel){
  switch (channel) {
  
    case 1:
      servoA.write(degreesOpen);                  // sets the servo position according to the scaled value
      Serial.println("Abriendo Canal A...");
    break;

    case 2:
      servoB.write(degreesOpen);                  // sets the servo position according to the scaled value
      Serial.println("Abriendo Canal B...");
    break;

    case 3:
      servoC.write(degreesOpen);                  // sets the servo position according to the scaled value
      Serial.println("Abriendo Canal C...");
    break;

    case 4:
      servoD.write(degreesOpen);                  // sets the servo position according to the scaled value
      Serial.println("Abriendo Canal D...");
    break;
  
    }
    
  }

//Funcion para cerrar el canal (servomotor) indicado.
int channelClose (int channel) {

switch (channel) {
  
    case 1:
      servoA.write(degreesClose);                  // sets the servo position according to the scaled value
      Serial.println("Cerrando Canal A...");
    break;

    case 2:
      servoB.write(degreesClose);                  // sets the servo position according to the scaled value
      Serial.println("Cerrando Canal B...");
    break;

    case 3:
      servoC.write(degreesClose);                  // sets the servo position according to the scaled value
      Serial.println("Cerrando Canal C...");
    break;

    case 4:
      servoD.write(degreesClose);                  // sets the servo position according to the scaled value
      Serial.println("Cerrando Canal D...");
    break;
  
    }
   }