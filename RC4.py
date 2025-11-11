def rc4(key, data):
    # KSA
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]

    # PRGA
    i = j = 0
    out = []
    for byte in data:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        out.append(byte ^ K)

    return bytes(out)
    
key_input = input("Nhập key: ")
plaintext_input = input("Nhập plaintext: ")

key = key_input.encode()          
pt = plaintext_input.encode()     

# Mã hóa
ct = rc4(key, pt)
print("Cipher (hex):", ct.hex())

# Giải mã
decrypted = rc4(key, ct)
print("Decrypted:", decrypted.decode())
