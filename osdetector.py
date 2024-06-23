import re
import sys
import platform
import os
import time

print('''


 _____       ______     _            _             
|  _  |      |  _  \   | |          | |            
| | | | ___  | | | |___| |_ ___  ___| |_ ___  _ __ 
| | | |/ __| | | | / _ \ __/ _ \/ __| __/ _ \| '__|
\ \_/ /\__ \ | |/ /  __/ ||  __/ (__| || (_) | |   
 \___/ |___/ |___/ \___|\__\___|\___|\__\___/|_|   
                                                   
               made by tunafeesh ~ sc4red2                              

''')
time.sleep(1)

def ping_host(ip):
    """
    Pings the given IP address and returns the TTL value from the response.
    """
    # Determine the ping command based on the OS
    if platform.system().lower() == "windows":
        command = f"ping -n 1 {ip}"
    else:
        command = f"ping -c 1 {ip}"

    # Execute the ping command
    process = os.popen(command)
    result = process.read()
    process.close()

    # Extract the TTL value from the ping response
    ttl_value = extract_ttl(result)
    return ttl_value

def extract_ttl(ping_response):
    """
    Extracts the TTL value from the ping response using regular expressions.
    """
    ttl_search = re.search(r"TTL=(\d+)", ping_response, re.IGNORECASE)
    if ttl_search:
        return int(ttl_search.group(1))
    return None

def detect_os(ttl):
    """
    Detects the operating system based on the TTL value.
    """
    if ttl is None:
        return "Unable to determine TTL value"

    if ttl >= 0 and ttl <= 64:
        return "Linux/Unix"
    elif ttl >= 65 and ttl <= 128:
        return "Windows"
    elif ttl >= 129 and ttl <= 254:
        return "Solaris/AIX"
    else:
        return "Unknown OS"

def main(ip):
    ttl = ping_host(ip)
    if ttl is not None:
        print(f"TTL value: {ttl}")
        os_type = detect_os(ttl)
        print(f"Detected OS: {os_type}")
    else:
        print("Failed to retrieve TTL value.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <IP address>")
        sys.exit(1)

    target_ip = sys.argv[1]
    main(target_ip)

