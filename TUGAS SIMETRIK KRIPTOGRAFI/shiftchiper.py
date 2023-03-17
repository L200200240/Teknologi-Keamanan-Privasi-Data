def encrypt(string, shift):
 
  chiper = ''
  for char in string:
    if char == ' ':
      chiper = chiper + char
    elif  char.isupper():
      chiper = chiper + chr((ord(char) + shift - 65) % 26 + 65)
    else:
      chiper = chiper + chr((ord(char) + shift - 97) % 26 + 97)
  
  return chiper
 
text = ("Tsabitta Najmining Ratri L200200240")
s = int("40")
print("plain text: ", text)
print("shift number: ", s)
print("decrypted: ", encrypt(text, s))
