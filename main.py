alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction == "encode":
  def encrypt(new_text,shift_num):
    encoded_word = ""
    for letter in new_text:
      position = alphabet.index(letter)
      new_position = position + shift_num
      new_letter = alphabet[new_position]
      encoded_word += new_letter 
    print(f"The encoded text is {encoded_word}")
elif direction == "decode":
  def encrypt(new_text,shift_num):
    decoded_word = ""
    spacer = 26
    for letter in new_text:
      position = alphabet.index(letter)
      new_position = (position + spacer) - shift_num
      new_letter = alphabet[new_position]
      decoded_word += new_letter
    print(f"The decoded text is {decoded_word}")  


encrypt(new_text=text,shift_num=shift)
