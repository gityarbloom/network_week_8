from network_tool.core.utils import *

def input_request():
    """מקבלת אינפוט משתמש"""
    inputting = input("ENTER A NUMBER BETWEEN 0 and 255: ")
    return inputting

def get_address():
    """תכנית לקבלת אינפוטים ליצירת כתובת IP תקינה"""
    address = ""
    for i in range(4):
        inputting = input_request()
        while not validation(inputting):
            print("WRONG INPUT")
            inputting = input_request()
        address += inputting
        address += "."
    return address

def get_mask_address():
    """תכנית לקבלת אינפוטים ליצירת כתובת MASK תקינה"""
    address = ""
    counter = 0
    while not validation_mask(address):
        if counter > 0:
            print("WRONG INPUT")
        address = get_address()
        counter += 1
    return address

if __name__ == "__main__":
    get_address()
    get_mask_address()