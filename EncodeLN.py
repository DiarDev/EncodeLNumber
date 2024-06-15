#!/usr/bin/python3
# encode file by Di4rDev
import string
import random

def encodeLNumber(input_string):
    long_number = int.from_bytes(input_string.encode(), byteorder='big')
    encoded_string = f"/#{long_number}"
    return encoded_string

def decodeLNumber(encoded_string):
    if not encoded_string.startswith("/#"):
        return "The encoded string is not in the correct format"
    
    long_number = int(encoded_string[2:])
    decoded_bytes = long_number.to_bytes((long_number.bit_length() + 7) // 8, byteorder='big')
    decoded_string = decoded_bytes.decode('utf-8')
    return decoded_string

def go():
    
    print("----------------------\n   1: encode\n   2: decode\n Input 1 or 2!\n----------------------\n")
    chon = str(input("Input: "))
    if chon == "1":
       code = str(input("Input code to encode: "))
       en = encodeLNumber(code)
       print(en)
    
    if chon == "2":
        code = (input("Input code to decode: "))
        de = decodeLNumber(code)
        print(de)
        
    if chon != "1" and chon != "2":
        go()
    
go()