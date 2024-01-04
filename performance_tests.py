from time import perf_counter
from serial_interface import SerialInterface


test_msgs = [
    # 18 bytes
    {
        "msg": "REQ"
    },
    # 162 bytes
    {
        "msg": "REQ",
        "data":
            "abcdefghijklmnopqrstuvwx \
            yz1234567890abcdefghijklm \
            nopqrstuvwxyz1234567890ab \
            cdefghijklmnopqrstuvwxyz1 \
            234567890abcdefghijklmnop \
            qrstuvwxyz12"
    },
    # 882 bytes
    {
        "msg": "REQ",
        "data0":
            "abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz12",
        "data1":
            "abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz12",
        "data2":
            "abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz12",
        "data3":
            "abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz12",
        "data4":
            "abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz12",
        "data5":
            "abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuv"
    }
]


if __name__ == "__main__":
    # Example usage
    iface = SerialInterface(port="COM5", baud=9600)
    msg = test_msgs[1]
    n = 1000

    start = perf_counter()

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
