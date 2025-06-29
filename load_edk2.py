#!/usr/bin/env python3
import usb.core
import struct
import sys
import argparse
import time

parser = argparse.ArgumentParser(description='Chainloads old pongoOS and boots EDK2.')

parser.add_argument('-p', '--pongo', dest='pongo', help='path to pongoOS')
parser.add_argument('-b', '--binary', dest='binary', help='path to edk2 binary')

args = parser.parse_args()

if args.pongo is None:
    print(f"error: No pongoOS image specified! Run `{sys.argv[0]} --help` for usage.")
    exit(1)

if args.binary is None:
    print(f"error: No binary specified! Run `{sys.argv[0]} --help` for usage.")
    exit(1)

dev = usb.core.find(idVendor=0x05ac, idProduct=0x4141)
if dev is None:
    print("Waiting for device...")

    while dev is None:
        dev = usb.core.find(idVendor=0x05ac, idProduct=0x4141)
        if dev is not None:
            dev.set_configuration()
            break
        time.sleep(2)
else:
    dev.set_configuration()

pongo = open(args.pongo, "rb").read()
binary = open(args.binary, "rb").read()

print("Loading pongo...")
pongo_size = len(pongo)
dev.ctrl_transfer(0x21, 2, 0, 0, 0)
dev.ctrl_transfer(0x21, 1, 0, 0, struct.pack('I', pongo_size))

dev.write(2, pongo, 1000000)
print("pongo loaded successfully.")

dev.ctrl_transfer(0x21, 4, 0, 0, 0)

print("Booting pongoOS...")
try:
    dev.ctrl_transfer(0x21, 3, 0, 0, "bootr\n")
except:
    # if the device disconnects without acknowledging it usually means it succeeded
    print("Should boot into pongoOS.")
time.sleep(2);

## Wait for USB again.
dev = usb.core.find(idVendor=0x05ac, idProduct=0x4141)
if dev is None:
    print("Waiting for device...")

    while dev is None:
        dev = usb.core.find(idVendor=0x05ac, idProduct=0x4141)
        if dev is not None:
            dev.set_configuration()
            break
        time.sleep(2)
else:
    dev.set_configuration()


print("Loading binary...")
binary_size = len(binary)
dev.ctrl_transfer(0x21, 2, 0, 0, 0)
dev.ctrl_transfer(0x21, 1, 0, 0, struct.pack('I', binary_size))

dev.write(2, binary, 1000000)
print("binary loaded successfully.")

dev.ctrl_transfer(0x21, 4, 0, 0, 0)

print("Booting binary...")

try:
    dev.ctrl_transfer(0x21, 3, 0, 0, "bootr\n")
except:
    # if the device disconnects without acknowledging it usually means it succeeded
    print("Success.")