alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encryption(plain_text, shift_key):
    cipher_text = ""
    for char in plain_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift_key) % 26
            cipher_text += alphabet[new_position]
        else:
            cipher_text += char
    return cipher_text

def decryption(cipher_text, shift_key):
    plain_text = ""
    for char in cipher_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position - shift_key) % 26
            plain_text += alphabet[new_position]
        else:
            plain_text += char
    return plain_text

wanna_end = False
while not wanna_end:
    ed = input("Type 'encrypt' for encryption , 'decrypt' for decryption:\n")   
    text = input("Type your message:\n")
    shift = int(input("Enter shift key:\n"))
    
    if ed == "encrypt":
        encrypted_text = encryption(plain_text=text.lower(), shift_key=shift)  
        print(f"Here is the text after encryption: {encrypted_text}")
    
    elif ed == "decrypt":
        decrypted_text = decryption(cipher_text=text.lower(), shift_key=shift) 
        print(f"Here is the text after decryption: {decrypted_text}")
    
    play_again = input("Type 'yes' to continue, Type 'no' to exit.\n").lower()
    if play_again == 'no':
        wanna_end = True
        print("Have a nice day! Bye..")
