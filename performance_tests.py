#!/usr/bin/env python3

"""Performance tests for Arduino - PC Interface"""

from time import sleep, perf_counter
from serial_interface import SerialInterface


test_msgs = [
    # 18 bytes
    {
        "msg":"REQ"
    },
    # 162 bytes
    {
        "msg":"REQ",
        "data":"abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz12"
    },
    # 882 bytes
    {
        "msg":"REQ",
        "data":"abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz12abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz12abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz12abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz12hijklmnopqrstuvwxyz12abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz12abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz12hijklmnopqrstuvwxyz"
    }
]


if __name__ == "__main__":
    # Example usage
    iface = SerialInterface(port="COM5", baud=115200)

    for num_test, msg in enumerate(test_msgs):

        print(f"Running test {num_test + 1}...")

        N = 1000
        RESP_COUNT = 0

        start = perf_counter()

        while RESP_COUNT < N:
            iface.write_msg(msg)  # Send it
            response = iface.read_msg()  # Read the response
            if response is not None:
                if response["msg"] == "ACK":
                    RESP_COUNT += 1

        end = perf_counter()

        execution_time = end - start
        time_per_msg = execution_time / RESP_COUNT
        print("\n")
        print(f"Received {RESP_COUNT} messages in {execution_time} s")
        print(f"{time_per_msg} s per round trip")

    iface.close()
