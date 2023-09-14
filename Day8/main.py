import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
end_of_program = False


def caesar(plain_text, shift_amount, direction_value):
    result_text = ""
    if direction_value == "decode":
        shift_amount *= -1
    for char in plain_text:
        if char in alphabet:
            pos = alphabet.index(char)
            result_text += alphabet[pos + shift_amount]
        else:
            result_text += char
    print(f"The {direction_value} text is {result_text}")


print(art.logo)
while not end_of_program:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    while direction not in ["encode", "decode"]:
        print("Invalid option!!!")
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift %= len(alphabet)
    caesar(text, shift, direction)
    restart = input('Do you wish to do it again? Type "y" or "n")\n').lower()
    while restart not in ["y", "n"]:
        print("Invalid option!!!")
        restart = input('Do you wish to do it again? Type "yes" or "no")\n').lower()
    if restart == "no":
        end_of_program = True
