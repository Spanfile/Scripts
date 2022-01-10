import socket
import fcntl
import struct
import http.client

IFACE = ""
CPANEL = ""
CPANEL_DDNS = ""
PREV_ADDR_LOCATION = "/var/ddns_prev_addr"


def get_iface_addr(ifname):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(
        fcntl.ioctl(
            sock.fileno(),
            0x8915,  # SIOCGIFADDR
            struct.pack("256s", bytes(ifname[:15], "utf-8")),
        )[20:24]
    )


def get_previous_addr():
    try:
        with open(PREV_ADDR_LOCATION) as f:
            return f.read()
    except Exception as e:
        print("Couldn't get previous address:", e)
        return None


def save_addr(addr):
    with open(PREV_ADDR_LOCATION, mode="w") as f:
        f.write(addr)


def call_ddns():
    client = http.client.HTTPSConnection(CPANEL)
    client.request("GET", CPANEL_DDNS)
    resp = client.getresponse()
    print(resp.read())


def main():
    prev_addr = get_previous_addr()
    current_addr = get_iface_addr(IFACE)

    if current_addr != prev_addr:
        print("Address changed", prev_addr, "->", current_addr)
        call_ddns()
        save_addr(current_addr)
    else:
        print("Address unchanged")


if __name__ == "__main__":
    main()
