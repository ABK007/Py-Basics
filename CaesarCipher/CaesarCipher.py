from logo import logo #Importing logo string from logo.py file 


#Tuple containing all 26 alphabets
alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')



def caesarCipher(): #Defining caesarcipher program
    
    """Encompases all the code for the program
    """
    
    print(logo) # Printing the logo at the start of the program. 
    
    while True: # While loop to run program continuously
        
        encodeOrDecode = input("Type 'encode' to encrypt and type 'decode' to decrypt: \n").lower() # asks user input to encode or decode
        
        input_text = input("Input your text here: \n").lower() # Asks user to type message for encryption or decryption
        
        shift = int(input("Type the shift number: \n")) # Asks user for shift number to shift alphabets by that number
        
        
        # Condition to apply modulus for shift number greater than 26 such as 100 or 45.
        if shift > 26:
            shift = shift % 26
    
    
        cipher = "" # initialized cipher string var to store the encrypted or decrypted code.
        
        # Following code will be executed when user selects for encoding text.
        if encodeOrDecode == "encode":
            
            # Executing for loop to iterate over input text.
            for letter in input_text:
                
                # Following code runs if the single element of input text is string. It finds the index number of that element
                # in the string and it will change its index by adding the shift number to encrypt text.
                if letter.isalpha() == True:
                    index = alphabet.index(letter)
                    shift_number = index + shift
                    
                    # if the index + shift number is greter than 26 then it will subtract that number by 26 to restart indexing 
                    # from 0 to 26
                    if shift_number >= 25:
                        shift_number = shift_number - 26
                    
                    # following code will look for alphabet in the alphabet tuple at that index according to shift_number.
                    # and then append that alphabet in the cipher string.
                    encrypt_letter = alphabet[shift_number]
                    cipher += encrypt_letter
                    
                # if single element of text is numeric then it will add in cipher string without any changes.    
                elif letter.isnumeric() == True:
                    cipher += letter
                
                # if single element of text is space then it will add in cipher string without any changes.    
                elif letter.isspace() == True:
                    cipher += letter
                    
                # if single element of text is other than numeric, space or alphabet then it will add in cipher string without any changes
                else:
                    cipher += letter
                
            print(f"your encoded message is:\n{cipher}") # Prints the encoded message
            
            
        
         # Following code will be executed when user selects for decoding text.
        elif encodeOrDecode == "decode":
            
            # Executing for loop to iterate over input text.
            for letter in input_text:
                
                # Following code runs if the single element of input text is string. It finds the index number of that element
                # in the string and it will change its index by adding the shift number to encrypt text.
                if letter.isalpha() == True:
                    index = alphabet.index(letter)
                    shift_number = index - shift
                    
                    # if the index - shift number is less than 0 then it will subtract that number by 26 to reverse the index number from 
                    # 26 to 0
                    if shift_number <= -1:
                        shift_number = shift_number + 26
                    
                    # following code will look for alphabet in the alphabet tuple at that index according to shift_number.
                    # and then append that alphabet in the cipher string.
                    encrypt_letter = alphabet[shift_number]
                    cipher += encrypt_letter
                
                # if single element of text is numeric then it will add in cipher string without any changes.
                elif letter.isnumeric() == True:
                    cipher += letter
                    
                # if single element of text is space then it will add in cipher string without any changes.
                elif letter.isspace() == True:
                    cipher += letter
                    
                # if single element of text is other than numeric, space or alphabet then it will add in cipher string without any changes.
                else:
                    cipher += letter
     
            print(f"your decoded message is:\n{cipher}") # Prints the decoded message

        playAgain = input("Do you want play again (yes/no): ").lower() # Asks the user to play again.
        
        if playAgain == "yes": # If input is yes than code will re-execute
            pass
        elif playAgain == "no": # if input is no then the while loop will end.
            print("Have a nice day, Goodbye") #prints goodbye message.
            break
        
        
            
 


caesarCipher()
