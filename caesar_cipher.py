# The listed alphabet here is used for getting the correct position of new letters after encoding/decoding. It is repeated to make sure that if the shift number would outrange the list, we won't get any errors
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# this is the main function to perform the modificaiton. You can also use two separate functions for encoding and decoding if this is confsing for you
def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  # checking the user's direction to make sure which operation to perform
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    # this if statement is for making sure that any character that is not an alphabet will be returened without any modifications
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
  print(f"Here's the {cipher_direction}d result: {end_text}")

# Here we have simply imported a graphic logo from another python file which is not nexessary for this program!
from art import logo
print(logo)

# This while loop is a way to ask for the user's decision to stop or continue decoding/encoding messages. Only whe the user chooses to stop will the program exit
should_end = False
while not should_end:

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  # this line of code is for making sure that the program will work correctly even if the user enters a shift that is greater than the number of letters in the alphabet
  shift = shift % 26

  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    should_end = True
    print("Goodbye")
    


