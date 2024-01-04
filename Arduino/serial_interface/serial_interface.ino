#include <ArduinoJson.h>
#include <String.h>

StaticJsonDocument<100> outgoing;
StaticJsonDocument<900> incoming;


void setup() {
  Serial.begin(9600);
  while (!Serial) continue;
}

void loop() { 
  if (Serial.available() > 0) {
    
      DeserializationError error = deserializeJson(incoming, Serial);
      
      if (error) {
        char error_msg[50];
        strcpy(error_msg, "Arduino Error: ");
        strcat(error_msg, error.c_str());
        outgoing["msg"] = error_msg;
  
      } else {   
      outgoing["msg"] = "ACK";       
      }
        
      serializeJson(outgoing, Serial);
      Serial.print('\n');
  }
}
