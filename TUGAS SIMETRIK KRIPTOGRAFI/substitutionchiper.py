import random

alphabet = 'abcdefghijklmnopqrstuvwxyz.,! '
key = 'nu.t!iyvxqfl,bcjrodhkaew spzgm'
plaintext = "Tsabitta Najmining Ratri"


def makeKey(alphabet):
   alphabet = list(alphabet)
   random.shuffle(alphabet)
   return ''.join(alphabet)

def encrypt(plaintext, key, alphabet):
    keyMap = dict(zip(alphabet, key))
    return ''.join(keyMap.get(c.lower(), c) for c in plaintext)

def decrypt(chiper, key, alphabet):
    keyMap = dict(zip(key, alphabet))
    return ''.join(keyMap.get(c.lower(), c) for c in chiper)

chiper = encrypt(plaintext, key, alphabet)

print("Plain text :", plaintext)
print("key :", key)
print("Chiper :", chiper)
print("Decrypted :", decrypt(chiper, key, alphabet))
