import art
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

def ceaser(original_text, shift_amount, encode_or_decode):
    output = ""
    if direction == "decode":
        shift_amount *= -1
    for letter in original_text:
        if letter in alphabet:
            shifted_number = alphabet.index(letter) + shift_amount
            shifted_number %= len(alphabet)
            output += alphabet[shifted_number]

        else:
            output += letter

    print(output)

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt or type 'decode' to decrypt:\n").lower()
    if direction not in ["encode", "decode"]:
        print("Invalid input")
    text = input("Type a text:\n").lower()
    shift = int(input("Type a number to shift your text\n"))


    ceaser(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart = input("Type 'yes' to continue. Otherwise, type 'no'").lower()
    if restart == "yes":
        should_continue = True
    else:
        should_continue = False