# osdetector

**osdetector** is a simple tool for detecting the operating system of a remote host based on the TTL (Time to Live) value of the ICMP echo packets it receives.

## Description

This script uses the ping command to send ICMP echo requests to the target IP address and extracts the TTL value from the response.
The TTL value is then used to determine the operating system of the target host by comparing it to predefined ranges.

## Usage

The script takes a single command-line argument, the IP address of the target host, and prints the TTL value and the detected operating system to the console.

### Example
 '''python osdetector.py 192.168.1.1
