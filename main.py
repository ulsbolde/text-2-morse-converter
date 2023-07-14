from tools import logo, morse

print(logo)

still_on = True

def convert2Morse(text):
  text = text.lower()
  
  if not text.isalnum():
    temp_text = ""
    for c in text:
      if c.isalnum() or c == " ":
        temp_text += c
    text = temp_text
  
  words = text.split(" ")
  text = ""
  for word in range(0, len(words)):
    words[word] = [*words[word]]
    
    for c in range(0, len(words[word])):
      words[word][c] = morse[words[word][c]]
    text += "   ".join(words[word]) + "       "
  return text.strip()

while still_on:
  text = input("\nEnter a text to convert to Morse Code: ")
  print(f"\nHere's your text in Morse Code: {convert2Morse(text)}\n")
  flag = input("Convert another? y/n ")
  if flag == 'n':
    still_on = False

print("\nThank you for using the Text to Morse Converter!")