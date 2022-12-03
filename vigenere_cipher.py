choice = ""

try:
    choice = input("Enter (0) for Encryption \nEnter (1) for Decryption \n")
except KeyboardInterrupt:
    print("KeyboardInterrupt Error")


def vigenere_encrypt():

    plaintext = input("Enter a message to Encrypt: ")
    key = input("Enter the encryption key:")
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    plaintext_int = [ord(i) for i in plaintext]
    ciphertext = ""

    for i in range(len(plaintext_int)):

        value = (plaintext_int[i] + (key_as_int[i % key_length])) % 26
        ciphertext += chr(value + 65)

    print("Encrypted Message: " + ciphertext)



def vigenere_decrypt():

    ciphertext = input("Enter the encrypted message: ")
    key = input("Enter the decryption key: ")
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    ciphertext_int = [ord(i) for i in ciphertext]
    plaintext = ""

    for i in range(len(ciphertext_int)):

        value = (ciphertext_int[i] - key_as_int[i % key_length]) % 26
        plaintext += chr(value + 65 + 26)

    print("Dencrypted Message: " + plaintext)

if choice == "0":
    vigenere_encrypt()
elif choice == "1":
    vigenere_decrypt()
else:
    print("The option you enterd is INVALID !")
