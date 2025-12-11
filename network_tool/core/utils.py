def binary_to_decimal(bin):
    """המרה מבינארי לעשרוני"""
    bin = int(bin, 2)
    return bin

def decimal_to_binary(address):
    """המרה מעשרוני לבינארי"""
    list_address = str.split(address, ".")
    address = ""
    for i in range(len(list_address)):
        dec = int(list_address[i])
        binary = bin(dec)[2:]
        address += "0" * (8-len(binary)) + str(binary) + "."
    return address[:-1]

def validation(inputting):
    """ולידציה לאינפוט של IP"""
    if int(inputting) > 255 or int(inputting) < 0:
        return False
    return True

def validation_mask(mask: str):
        """ולידציה לכתובת המאסק שהזין המשתמש 
        (שיש לה 4 אוקטטות ושהיא בסדר ההיררכי הנכון)"""
        list_mask = str.split(mask, ".")
        if len(list_mask) < 4:
             return False
        for i in range(len(list_mask)):
            if i == 0:
                continue
            if int(list_mask[i]) != 0 and int(list_mask[i-1]) != 255:
                return False
            if int(list_mask[i]) != 0 and i != 3:
                return False
            if i == 3 and int(list_mask[i] == 255):
                return False
            if int(list_mask[i]) > int(list_mask[i-1]):
                return False
        return True

def result_net_address(ip, mask):
    ip = decimal_to_binary(ip)
    mask = decimal_to_binary(mask)
    net_address = ""
    ip_list = []
    mask_list = []
    for i in range(32):
        if ip[i] == ".":
            continue
            if mask[i] == ".":
                continue
        ip_list.append(int(ip[i]))
        mask_list.append(int(mask[i]))
        for i in range(len(ip_list)):
            aoct = ip_list[i] and mask_list[i]       
            net_address += str(aoct)
        net_address += "."
    return net_address