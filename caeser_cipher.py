choice = ""

try:
    choice = input("Enter (0) for Encryption \nEnter (1) for Decryption \n")
except KeyboardInterrupt:
    print("KeyboardInterrupt Error")

#Encrypion Code
def ceaser_encrypt(): 
    result = "" 
    text = input("Enter the text to Encrypt: ")

    try:
        s = int(input("Enter the Number of Shift's: "))
    except ValueError:
        print("Please enter number:-")

    # traverse text 
    try:
        for i in range(len(text)):  #len finding lenght
         char = text[i] 
  
         # Encrypt uppercase characters 
         if (char.isupper()): 
            result += chr((ord(char) + s-65) % 26 + 65) 
  
         # Encrypt lowercase characters 
         else: 
            result += chr((ord(char) + s - 97) % 26 + 97) 

        print("Dencrypted Data:  " + result) 
    except UnboundLocalError:
        print("Shift value must be a number! )")

#Dencrypion Code
def ceaser_dencrypt(): 
    result = "" 
    text = input("Enter the text to Dencrypt: ")

    try:
        s =26 - int(input("Enter the Number of Shift's: "))
    except ValueError:
        print("Please enter number!")

    # traverse text 
    try:
        for i in range(len(text)):  #len finding lenght
         char = text[i] 
  
         # Encrypt uppercase characters 
         if (char.isupper()): 
            result += chr((ord(char) + s-65) % 26 + 65) 
  
         # Encrypt lowercase characters 
         else: 
            result += chr((ord(char) + s - 97) % 26 + 97) 

        print("Dencrypted Data:  " + result) 
    except UnboundLocalError:
        print("Shift value must be a number between (1 to 26)! )")
  

if choice == "0":
    ceaser_encrypt()
elif choice == "1":
    ceaser_dencrypt()
else:
    print("The option you enterd is INVALID !")
