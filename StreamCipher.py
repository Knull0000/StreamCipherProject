import random

def generate_keystream(key, length):
    random.seed(key)  
    return [random.randint(0, 255) for _ in range(length)]

def encrypt_stream(plaintext, key):
    keystream = generate_keystream(key, len(plaintext))
    ciphertext = [p ^ k for p, k in zip(plaintext, keystream)]
    return ciphertext

def decrypt_stream(ciphertext, key):
    keystream = generate_keystream(key, len(ciphertext))
    plaintext = [c ^ k for c, k in zip(ciphertext, keystream)]
    return plaintext

message = input("Nhập thông điệp cần mã hóa: ")
key = int(input("Nhập key (số nguyên): "))

plaintext = [ord(c) for c in message]

ciphertext = encrypt_stream(plaintext, key)
print("Ciphertext:", ciphertext)

decrypted = decrypt_stream(ciphertext, key)
decrypted_message = ''.join(chr(c) for c in decrypted)

print("Decrypted:", decrypted_message)
