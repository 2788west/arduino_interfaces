#include <ArduinoJson.h>

StaticJsonDocument<500> outgoing; // JSON Document to hold data to be sent
StaticJsonDocument<500> incoming; // JSON Document to hold data being received

void setup() {
  Serial.begin(115200);
  while (!Serial);
}

void loop() { 
  if (Serial.available() == 0) return;

  DeserializationError error = deserializeJson(incoming, Serial); // Parse JSON directly from the Serial port

  // If a parsing error occurs, send the error message back to the sender
  if (error) outgoing["msg"] = "Arduino Error: " + String(error.c_str());

  // If the message was "Request", we send "Acknowledge
  else if (incoming["msg"] == "REQ") {
    outgoing["msg"] = "ACK";
    // Add additional data here, examples below:
    // outgoing["data"] = 0.34;
    // outgoing["sensor} = "temperature";
  }
  // Otherwise, we send "Unrecognized Request"
  else outgoing["msg"] = "Unrecognized Request";
   
  serializeJson(outgoing, Serial); // Serialize the message and send it back to the serial port
  Serial.print('\n'); // Since we use "readline()" in Python, we need to add the newline character
}
