def encrypt(string, shift):
 
  cipher = ''
  for char in string:
    if char == ' ':
      cipher = cipher + char
    elif  char.isupper():
      cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)
    else:
      cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)
  
  return cipher
 
text = ("Tsabitta Najmining Ratri L200200240")
s = int("40")
print("plain text: ", text)
print("shift number: ", s)
print("decrypted: ", encrypt(text, s))
