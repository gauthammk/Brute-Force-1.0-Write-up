print('Offset = ', ord('N') - ord('H'))
msg = 'NK{Xuzgzk_Sk_ZU_Mkz_Vuotzy}'
abc = "abcdefghijklmnopqrstuvwxyz"
shift = ord('H') - ord(msg[0])
secret = ''
for c in msg:
    if c in abc:
        secret += abc[(abc.find(c)+shift) % 26]
    else:
        secret += c

print(secret)
