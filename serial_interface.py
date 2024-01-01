#!/usr/bin/env python3

""" Arduino PC Interface for Data Logging"""

from serial import Serial
import json
from time import perf_counter, sleep


class SerialInterface:
    def __init__(self, port="COM5", baud=115200, timeout=1):
        self.ser = Serial(port, baudrate=baud, timeout=timeout)
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
    start = perf_counter()
    iface = SerialInterface()
    msg = {"msg": "ping"}

    n = 10000

    while iface.r < n:
        # Check if response was received
        iface.write_msg(msg)
        iface.read_msg()

    end = perf_counter()
    execution_time = end - start
    time_per_msg = execution_time / n
    print("\n")
    print(f"Received {iface.r} messages in {execution_time} s")
    print(f"{time_per_msg} s per round trip")
