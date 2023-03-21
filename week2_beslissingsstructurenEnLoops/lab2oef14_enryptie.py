alfabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

encrypt = input("encrypt or decrypt? ")
woord = input("geef een woord: ")
shift = int(input("wat is de shift? "))

def CryptDecrypt(word, shift, encrypt):
        crypt = ""
        
        for i in word:
            index = alfabet.index(i.lower())

            if (encrypt == "encrypt"):
                cryptChar = alfabet[index + shift]
            elif (encrypt == "decrypt"):
                cryptChar = alfabet[index - shift]
            
            if (i.isupper()):
                cryptChar = cryptChar.upper()
            
            crypt += cryptChar
        return crypt

print(f"{woord} = {CryptDecrypt(woord, shift, encrypt)}")




