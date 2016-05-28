
def hex_to_text(hex):
    return ''.join([chr(int(hex[i:i+2],16)) for i in range(0,len(hex),2)])
