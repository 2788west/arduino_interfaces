#!/usr/bin/env python3

""" Arduino PC Interface for Data Logging"""

import json
from serial import Serial
from time import sleep


class SerialInterface:
    def __init__(self, port="COM1", baud=9600):
        self.ser = Serial(port, baudrate=baud)
        self.no_response = False
        self.r = 0
        sleep(5)

    def read_msg(self):
        """Reads a line from the serial buffer,
        decodes it and stores its contents as a dict."""
        if self.ser.in_waiting > 0:
            incoming = self.ser.readline().decode("utf-8")
            self.no_response = False
            try:
                response = json.loads(incoming)
                print(f"Received: {response['msg']}")
                self.r += 1
            except json.JSONDecodeError:
                print("Error decoding JSON message!")

        else:
            self.no_response = True

    def write_msg(self, message=None):
        """Sends a JSON-formatted command to the serial
        interface."""
        if self.no_response:
            return
        else:
            try:
                json_msg = json.dumps(message) + '\n'
                self.ser.write(json_msg.encode())
                print(f"Sent: {message['msg']}")
            except TypeError:
                print("Unable to serialize message.")


if __name__ == "__main__":
    # Example usage
    iface = SerialInterface()
    msg = {"msg": "REQ"}  # Define the message
    iface.write_msg(msg)  # Send it
    iface.read_msg()  # Read the response

