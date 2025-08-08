import random as r
import string as s

def encrypt(msg_bits, image):
   
    num = r.randrange(1,256)
    l = len(msg_bits)
    
    characters = s.ascii_letters + s.digits + s.punctuation
    key = ''.join(r.choices(characters, k=10)) 
    
    enc_bits = []
    for i in msg_bits:
        enc_bits.append(i^num) 
    
    image[1][0][2] = num
    
    for i in range(1, len(key)+1):
        image[1][i][2] = ord(key[i-1])
    
    return key, enc_bits, image

def decrypt(img, key):
    
    num = img[1][0][2]
    l = len(key)
    
    for i in range(1, l + 1):
        if img[1][i][2] != ord(key[i-1]):
            return "Decryption failed: Incorrect Key."

    dec_list = []
    message_length = img[0][0][2]

    for i in range(1, message_length + 1):
        dec_list.append(img[0][i][2] ^ num)
        
    return ''.join([chr(i) for i in dec_list])