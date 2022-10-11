from logo import logo


alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')





def caesarCipher():
    print(logo)
    
    while True:
        encodeOrDecode = input("Type 'encode' to encrypt and type 'decode' to decrypt: \n").lower()
        input_text = input("Input your text here: \n").lower()
        shift = int(input("Type the shift number: \n"))
        
        if shift > 26:
            shift = shift % 26
    
    

        cipher = ""
        if encodeOrDecode == "encode":
            for letter in input_text:
                if letter.isalpha() == True:
                    index = alphabet.index(letter)
                    shift_number = index + shift
                    if shift_number >= 25:
                        shift_number = shift_number - 26
                    encrypt_letter = alphabet[shift_number]
                    cipher += encrypt_letter
                elif letter.isnumeric() == True:
                    cipher += letter
                elif letter.isspace() == True:
                    cipher += letter
                else:
                    cipher += letter
                
            print(f"your encoded message is:\n {cipher}")
    
        elif encodeOrDecode == "decode":
            for letter in input_text:
                if letter.isalpha() == True:
                    index = alphabet.index(letter)
                    shift_number = index - shift
                    if shift_number <= -1:
                        shift_number = shift_number + 26
                    encrypt_letter = alphabet[shift_number]
                    cipher += encrypt_letter
                elif letter.isnumeric() == True:
                    cipher += letter
                elif letter.isspace() == True:
                    cipher += letter
                else:
                    cipher += letter
     
            print(f"your decoded message is:\n {cipher}")

        playAgain = input("Do you want play again (yes/no): ").lower()
        
        if playAgain == "yes":
            pass
        elif playAgain == "no":
            break
        
            
 


caesarCipher()
