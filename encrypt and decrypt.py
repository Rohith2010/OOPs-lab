#Create a function called encrypt that takes some text(String) and a Shift(Integer)and then encrypts the text using the Caesar Cipher algorithm, returning the encrypted text.
#Create a second function to decrypt an encrypted string, using the same input parameters and returning the decrypted text.
def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            shifted_char = chr((ord(char) + shift - ord('A' if is_upper else 'a')) % 26 + ord('A' if is_upper else 'a'))

            encrypted_text += shifted_char
        else:
            encrypted_text += char

    return encrypted_text

def decrypt(encrypted_text, shift):
    return encrypt(encrypted_text, -shift)
text_to_encrypt = "Hello, World!"
shift_amount = 6
encrypted_result = encrypt(text_to_encrypt, shift_amount)
print(f"Encrypted Text: {encrypted_result}")
decrypted_result = decrypt(encrypted_result, shift_amount)
print(f"Decrypted Text: {decrypted_result}")


Encrypted Text: Nkrru, Cuxrj!
Decrypted Text: Hello, World!
