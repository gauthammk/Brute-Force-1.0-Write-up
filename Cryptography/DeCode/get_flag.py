import base64

encoded_text = '''Vm0xNFUxRXhXWGhYV0dSUFUwZG9WRmx0ZUV0V1J
teDBUbFZPYUZKc2NIbFdNalZMWVRBeFdGVnJXbFpXZWxaUV
dXdGtTMVpyTVZWWGJHUlRaV3haZWxkV1pIcGtNbEYzVGxa
b1RsWnRhRmhaYkZwR1pERmtXV05GWkdsaVZscElWbTAxVjF
WdFNsaGxSbWhWVm14d00xcEZXbHBsVlRGSllVWk9UbEpGV1h
kV1ZFWnZaREZhU0ZOdVNsUmlhM0JYV1ZkMFlWbFdVbk5TVkd4
UlZWUXdPUT09'''
decoded_text = base64.b64decode(encoded_text)
while True:
    if 'HE' in decoded_text.decode():
        print(decoded_text.decode())
        break
    decoded_text = base64.b64decode(decoded_text)
