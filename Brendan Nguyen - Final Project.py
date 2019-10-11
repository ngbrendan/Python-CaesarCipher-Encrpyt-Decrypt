# -*- coding: utf-8 -*-
"""
Brendan Nguyen
Harris/CS1311
Final Project
File Encryptor/Decryptor with Caesar Cipher
"""
from os import path

def encrypt(text,s): 
    encrypted = "" 

    for i in range(len(text)): 
        char = text[i] 
  
        if char==' ':
            encrypted+=' '     
        elif char=='\n':
            encrypted+='\n'      
        elif char=='.':
            encrypted+='.'     
        elif (char.isupper()): 
            encrypted += chr((ord(char) + s - 65) % 26 + 65)
        else: 
            encrypted += chr((ord(char) + s - 97) % 26 + 97) 
  
    return encrypted

def decrypt(text,s): 
    decrypted = "" 
  
    for i in range(len(text)): 
        char = text[i] 
        
        if char==' ':
            decrypted+=' '  
        elif char=='\n':
            decrypted+='\n'         
        elif char=='.':
            decrypted+='.'        
        elif (char.isupper()): 
            decrypted += chr((ord(char) - s - 65) % 26 + 65) 
        else: 
            decrypted += chr((ord(char) - s - 97) % 26 + 97) 
    
    return decrypted

def validate_positive_integer(key):
    
    while True:
        try:
            key=int(input("What positive number would you like your key to be? "))
            if(key<=0):
                raise ValueError
            break
        except ValueError:
            print("The value needs to be a positive number.")
    return key
  
def editfile(filename, choice):
    
    if choice == 'encrypt':
        print("Now Encrypting...")
        s = 0
        
        s = validate_positive_integer(s)
        print()
        
        readfile = open(filename, 'r')
        filecontent = readfile.read()
        readfile.close() 
        outfile = open(filename, 'w')
        result = encrypt(filecontent,s)
        outfile.write(str(s))
        outfile.write('\n')
        outfile.write(result)
        outfile.close()

    else:
        print("Now Decrypting...\n")
        readfile = open(filename, 'r')
        filecontent = readfile.readline().strip()
        s = filecontent
        CanDecrypt = True
        
        try:
            s = int(s)
        except ValueError:
            result = "Error: No key found. Cannot Decrypt."
            CanDecrypt = False
        
        if (CanDecrypt == True):
            filecontent = readfile.read()
            readfile.close()
            outfile = open(filename, 'w')
            result = decrypt(filecontent, int(s))
            outfile.write(result)
            outfile.close()
            
    return result

def main():
    response = 'y'
    while (response == 'y') or (response == 'Y'):
        filename = input("What file would you like to encrypt/decrypt: ")
        
        while path.exists(filename) == False:
            filename = input("File does not exist. Please enter a existing file: ")
        
        print("The file contents are: \n")
        readfile = open(filename,'r')
        print(readfile.read())
        
        choice = input("Would you like to encrypt or decrypt? ")
        
        while (choice != "encrypt") and (choice != "decrypt"):
            choice = input("Please choose enter 'encrypt' or 'decrypt': ")
        
        print(editfile(filename,choice))
        
        response = input("Would you like to continue? (y/Y): ")
    
main()


    