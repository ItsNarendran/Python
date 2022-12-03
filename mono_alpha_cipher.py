mono_alpha = {
    'a':'z','A':'Z','1':'2',
    'b':'y','B':'Y','2':'1',
    'c':'x','C':'X','3':'4',
    'd':'w','D':'W','4':'3',
    'e':'v','E':'V','5':'6',
    'f':'u','F':'U','6':'5',
    'g':'t','G':'T','7':'8',
    'h':'s','H':'S','8':'7',
    'i':'r','I':'R','9':'0',
    'j':'q','J':'Q','0':'9',
    'k':'p','K':'P',
    'l':'o','L':'O',
    'm':'n','M':'N',
    'n':'m','N':'M',
    'o':'l','O':'L',
    'p':'k','P':'K',
    'q':'j','Q':'J',
    'r':'i','R':'I',
    's':'h','S':'H',
    't':'g','T':'G',
    'u':'f','U':'F',
    'v':'e','V':'E',
    'w':'d','W':'D',
    'x':'c','X':'C',
    'y':'b','Y':'B',
    'z':'a','Z':'A',
}

mono_alpha_ency_list = []
choice = ""

try:
    choice = input("Enter (0) for Encryption \nEnter (1) for Decryption \n")
except KeyboardInterrupt:
    print("KeyboardInterrupt Error")



def mono_alpha_ency(): 
    text = input("Enter the text to Encrypt: ")
    for letters in text:
        mono_alpha_ency_list.append(mono_alpha[letters])
    print(*mono_alpha_ency_list, sep ="") 

def mono_alpha_decy(): 
    text = input("Enter the text to Decrypt: ")
    for letters in text:
        mono_alpha_ency_list.append(mono_alpha[letters])
    print(*mono_alpha_ency_list, sep ="") 


if choice == "0":
    mono_alpha_ency()
elif choice == "1":
    mono_alpha_decy()
else:
    print("The option you enterd is INVALID !")
