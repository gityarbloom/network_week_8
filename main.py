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

# from core.utils import *


# def net_address_by_mask():
#     my_data = {}
#     mask = input("\nPLEASE ENTER A S.B. MASK \n--(10 NUMBERS BETWEEN 0 TO 1 ONLY, ONES FIRST AND THE ZEROS AT THE END): ")
#     while not validate_mask(mask):
#         mask = input("\nPLEASE ENTER A S.B. MASK \n--(10 NUMBERS BETWEEN 0 TO 1 ONLY, ONES FIRST AND THE ZEROS AT THE END): ")
#     my_data["Binary Mask Input: "] = mask

#     dec_ip_number = int(input("\nPLEASE ENTER A NUMBER BETWEEN 0 AND 1023: "))
#     while not validate_dec(dec_ip_number):
#         dec_ip_number = int(input("\nPLEASE ENTER A NUMBER BETWEEN 0 AND 1023: "))
#     my_data["Decimal Input: "] = dec_ip_number
#     my_data["Input in Binary: "] = decimal_to_binary(dec_ip_number)

#     dec_ip_number = decimal_to_binary(dec_ip_number)
#     bin_ip_address = split_by_mask(mask, dec_ip_number)
#     my_data["Left Part (Binary): "] = bin_ip_address[0]
#     my_data["Right Part (Binary): "] = bin_ip_address[1]
#     my_data["Resultin Decimal: "] = dec_ip_by_mask(bin_ip_address)
#     return my_data

# def update_data(my_data: dict):
#     with open("bit_mask_result_211846894.txt", "a") as data:
#         data.write("\n" + "*" * 15)
#         data.write("\n")
#         for key, value in my_data.items():
#             new_row = str(key) + str(value)
#             data.write(new_row)
#             data.write("\n")
#         return

# if __name__ == "__main__":
#     my_data = net_address_by_mask()
#     update_data(my_data)

if __name__ == "__main__":
    get_address()
    get_mask_address()