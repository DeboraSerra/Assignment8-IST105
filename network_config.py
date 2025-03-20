import random
import sys


def define_ipv6(mac_address):
    ipv6 = None
    ipv6 = f"2001:db8::{mac_address[0:2]}{mac_address[3:5]}:{mac_address[6:8]}{mac_address[9:11]}:{mac_address[12:14]}{mac_address[15:17]}"
    return ipv6


def define_ipv4():
    ipv4 = None
    ipv4 = f"192.168.1.{random.randint(1, 254)}"
    return ipv4


def validate_mac_address(mac_address):
    if len(mac_address) != 17:
        print("Invalid MAC address size")
        return False
    elif (
        mac_address.count(":") != 5
    ):
        print("Invalid MAC address format")
        return False
    elif not all(
        c in "0123456789abcdef"
        for c in mac_address.replace(":", "").lower()
    ):
        print("Invalid MAC address characters")
        return False
    return True


def validate_dhcp(dhcp):
    if dhcp not in ["4", "6"]:
        print("Invalid DHCP version")
        return False
    return True


def validate_ipv4(ip, lease_db):
    if not ip:
        return True
    all_ips = [lease_db[mac]["ipv4"] for mac in lease_db]
    if ip in all_ips:
        print("IPv4 address already in use")
        return False
    elif ip not in [f"192.168.1.{i}" for i in range(255)]:
        print("Invalid IPv4 address")
        return False
    return True


def lease_ips():
    mac_address, dhcp = sys.argv[1], sys.argv[2]
    lease_db = {}
    if not validate_mac_address(mac_address) or not validate_dhcp(dhcp):
        return
    ipv4, ipv6 = None, None
    if dhcp == "4":
        ipv4 = define_ipv4()
    else:
        ipv6 = define_ipv6(mac_address)

    while not validate_ipv4(ipv4, lease_db):
        ipv4 = define_ipv4()

    # lease time 1 hour
    lease_time = 3600
    break_line = "</br>"

    if mac_address in lease_db:
        lease_db[mac_address] = {"ipv4": f"{ipv4}/24", "ipv6": f"{ipv6}/64"}
    else:
        lease_db[mac_address] = {
            "ipv4": f"{ipv4}/24",
            "ipv6": f"{ipv6}/64",
            "lease_time": lease_time,
        }
    print(f"mac_address: {mac_address}")
    print(break_line)
    print(f"DHCP version: DHCPv{dhcp}")
    print(break_line)
    if ipv4:
        print(f"ipv4: {ipv4}")
    if ipv6:
        print(f"ipv6: {ipv6}")
    print(break_line)
    print(f"lease_time: {lease_time}")


if __name__ == "__main__":
    lease_ips()
