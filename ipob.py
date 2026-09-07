##########################################################
#                          IPOB                          #
#                                                        #
#   This is IPOB, a small utility I made to obfuscate IP\#
#V4 addresses. It supports dotted hexadecimal, standard \#
#hexadecimal, dotted octal, and decimal. It is very ligh\#
#tweight and has no dependencies.                        #
##########################################################

##########################################################
#                          Usage                         #
#   It is very simple to use. Run it and enter the IP yo\#
#want to obfuscate into the various formats. These forma\#
#ts are accepted by most standard web browsers and progr\#
#ams. This doesn't provide anonymity, only the textual r\#
#epresentation of the IP address itself.                 #
#   This version currently does not have proper error ha\#
#ndling and was written in a rush, I apologize for any i\#
#nconvenience that this causes for anyone using this pro\#
#gram.                                                   #
##########################################################

##########################################################
#                          Author                        #
#   This program was written by zero___                  #
##########################################################

import ipaddress

def convert_to_hex(num1, num2, num3, num4):
    # :02x formats as lowercase hex, minimum 2 digits, padding with 0
    return f"0x{num1:02x}", f"0x{num2:02x}", f"0x{num3:02x}", f"0x{num4:02x}"

def convert_to_standard_hex(num1, num2, num3, num4):
    # convert from string > 32 bit int > decimal > hexadecimal
    ipv4_str = f"{num1}.{num2}.{num3}.{num4}"
    dec_ip = int(ipaddress.ip_address(ipv4_str))
    hex_ip = hex(dec_ip)
    return hex_ip

def convert_to_oct(num1, num2, num3, num4):
    # :03o formats as octal, minimum 3 digits, padded with 0 (e.g., 0177)
    return f"0{num1:03o}", f"0{num2:03o}", f"0{num3:03o}", f"0{num4:03o}"

def convert_to_dec(num1, num2, num3, num4):
    ipv4_str = f"{num1}.{num2}.{num3}.{num4}"
    return int(ipaddress.ip_address(ipv4_str))

def print_results(hex_part1, hex_part2, hex_part3, hex_part4, oct_part1, oct_part2, oct_part3, oct_part4, hex_ip, dec_ip):
    print(f"Standard hex: {hex_ip}")
    print(f"Dotted hex: {hex_part1}.{hex_part2}.{hex_part3}.{hex_part4}")
    print(f"Oct: {oct_part1}.{oct_part2}.{oct_part3}.{oct_part4}")
    print(f"Standard decimal: {dec_ip}")

def intro():
    print(r"/...... ......  ....  ...\ ")
    print(r"\  ..   ..   . .    . .../ ")
    print(r"/  ..   ...... .    . ...\ ")
    print(r"\...... ..      ....  .../ ")

def start():
    intro()
    num1, num2, num3, num4 = map(int, input("Enter an IP to obfuscate: ").split('.'))
    hex_part1, hex_part2, hex_part3, hex_part4 = convert_to_hex(num1, num2, num3, num4)
    oct_part1, oct_part2, oct_part3, oct_part4 = convert_to_oct(num1, num2, num3, num4)
    hex_ip = convert_to_standard_hex(num1, num2, num3, num4)
    dec_ip = convert_to_dec(num1, num2, num3, num4)
    print_results(hex_part1,
                  hex_part2, 
                  hex_part3, 
                  hex_part4, 
                  oct_part1, 
                  oct_part2, 
                  oct_part3, 
                  oct_part4, 
                  hex_ip, 
                  dec_ip)

if __name__ == "__main__":
    start()