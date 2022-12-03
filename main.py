opt = ""

print("\nChose the Encryption type:-\n")

try:
	opt = int(
	    input(
	        "1.Monoalphabetic Cipher\n2.Ceaser Cipher\n3.Vigenere Cipher\n4.enigma_cipher.py"
	    ))
except ValueError:
	print("Please enter number:-")
except KeyboardInterrupt:
	print("Keyboard Interrupted")

if opt == 1:
	try:
		import mono_alpha_cipher
	except ModuleNotFoundError:
		print("Requested Encryption type not found!")
elif opt == 2:
	try:
		import ceaser_cipher
	except ModuleNotFoundError:
		print("Requested Encryption type not found!")
elif opt == 3:
	try:
		import vigenere_cipher
	except ModuleNotFoundError:
		print("Requested Encryption type not found!")
elif opt == 4:
	try:
		import enigma_cipher
	except ModuleNotFoundError:
		print("Requested Encryption type not found!")
else:
	print("The option you enterd is INVALIDn !")
