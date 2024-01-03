#include <ArduinoJson.h>

StaticJsonDocument<512> outgoing;
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
    outgoing["name"] = "John Doe";
    outgoing["age"] = 28;
    outgoing["email"] = "johndoe@example.com";
    outgoing["street"] = "123 Main St";
    outgoing["city"] = "Anytown";
    outgoing["state"] = "Anystate";
    outgoing["newsletter"] = true;
    outgoing["notifications"] = false;
    outgoing["theme1"] = "dark";
    outgoing["theme2"] = "light";
    outgoing["purchase1"] = "book";
    outgoing["purchase2"] = "laptop";
    outgoing["purchase3"] = "pen";
    outgoing["purchase4"] = "notebook";
    outgoing["purchase5"] = "headphones";
    outgoing["purchase6"] = "backpack";
    outgoing["purchase6"] = "chair";
    outgoing["purchase6"] = "desk lamp";
    outgoing["membership_level"] = "gold";
    outgoing["favorite_color"] = "blue";
    outgoing["phone_numer"] = "555-1234";
    outgoing["employment_status"] = "employed";
    outgoing["salary"] = 60000;
    outgoing["car_model"] = "Sedan";
    outgoing["car_year"] = 2020;
    
    serializeJson(outgoing, Serial);
    Serial.print('\n');
    }  
  }
}
