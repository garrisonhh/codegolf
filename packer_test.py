text = b"the quick brown fox jumped over the lazy dog"


info = 0xABC

# inject 3 bytes of info into a 4-byte char
char = 0xF0 | (info & 7)
info >> 3
for i in range(3):
    char <<= 8
    char |= 8 | (info & 63)
    info >> 6

print("encoded:", hex(char))

# retrieve 3 bytes of info from a 4-byte char
