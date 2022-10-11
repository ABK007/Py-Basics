from logo import logo


alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')


print(logo)
print("\n")

encodeOrDecode = input("Type 'encode' to encrypt and type 'decode' to decrypt: \n").lower()
input_text = input("Input your text here: \n").lower()
shift = int(input("Type the shift number: \n"))

def encrypt(text, shift):
    encrypted_text = ""
    for letter in text:
        index = alphabet.index(letter)
        shift_number = index + shift
        if shift_number >= 25:
            shift_number = shift_number - 26
        encrypt_letter = alphabet[shift_number]
        encrypted_text += encrypt_letter
    return encrypted_text

def decrypt(text, shift):
    encrypted_text = ""
    for letter in text:
        index = alphabet.index(letter)
        shift_number = index - shift
        if shift_number <= -1:
            shift_number = shift_number + 26
        encrypt_letter = alphabet[shift_number]
        encrypted_text += encrypt_letter
    return encrypted_text


if encodeOrDecode == "encode":
    print(encrypt(input_text, shift))
elif encodeOrDecode == "decode":
    print(decrypt(input_text, shift))
