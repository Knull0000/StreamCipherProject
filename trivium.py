def str2bits(s,n): return [(ord(c)>>i)&1 for c in s for i in range(8)][:n]+[0]*(n-len(s)*8)
def trivium(key,iv,n):
    s1,s2,s3 = key+[0]*(93-len(key)), iv+[0]*(84-len(iv)), [0]*108+[1,1,1]
    ks=[]
    for _ in range(n):
        t1 = s1[65]^(s1[90]&s1[91])^s1[92]^s2[77]
        t2 = s2[68]^(s2[81]&s2[82])^s2[83]^s3[86]
        t3 = s3[65]^(s3[108]&s3[109])^s3[110]^s1[68]
        ks.append(t1^t2^t3)
        s1=[t1]+s1[:-1]; s2=[t2]+s2[:-1]; s3=[t3]+s3[:-1]
    return ks
def xor_bits(bits,data):
    r=bytearray()
    for i,b in enumerate(data):
        byte=0
        for j in range(8): byte |= ((b>>j)&1 ^ (bits[i*8+j] if i*8+j<len(bits) else 0))<<j
        r.append(byte)
    return bytes(r)

msg = input("Plaintext: ").encode()
key = str2bits(input("Key(4 ký tự): "),80)
iv = str2bits(input("IV(3 ký tự): "),80)

# Mã hóa
ks = trivium(key,iv,len(msg)*8)
cipher = xor_bits(ks,msg)
print("Cipher(hex):",cipher.hex())

# Giải mã
ks2 = trivium(key,iv,len(cipher)*8)
print("Decrypted:", xor_bits(ks2,cipher).decode())
