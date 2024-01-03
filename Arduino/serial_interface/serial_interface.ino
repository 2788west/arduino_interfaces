#include <ArduinoJson.h>

StaticJsonDocument<20> outgoing;
StaticJsonDocument<20> incoming;

void setup() {
  Serial.begin(9600);
  while (!Serial) continue;
}

void loop() { 
  if (Serial.available() > 0) {

    String jsonData = Serial.readStringUntil('\n');    
    DeserializationError error = deserializeJson(incoming, jsonData);
    
    if (error) {
      Serial.print("deserializeJson() failed: ");
      Serial.println(error.c_str());

    } else {   
    outgoing["msg"] = "ACK";
     serializeJson(outgoing, Serial);
    Serial.print('\n');
    }  
  }
}
