from pwn import xor

with open("encrypted.txt", "r") as f:
	enc = f.read()
print(enc)

dec = xor(enc, "ccsc")
print(dec.decode())