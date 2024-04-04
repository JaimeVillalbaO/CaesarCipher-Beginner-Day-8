import acsi_day8

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# print(alphabet.index('a'))
# print(len(alphabet))
print(acsi_day8.logo)



def caesar(start_text, shif_amount, cipher_direction):
    end_text = ''

    if shif_amount > 26:
        shif_amount = shif_amount % 26 
    
    if cipher_direction == 'decode':
            shif_amount = shif_amount *-1
    
    for char in start_text:
        if char not in alphabet: 
             end_text += char
             continue
        word_position = alphabet.index(char)
        new_position = word_position + shif_amount
        end_text += alphabet[new_position]
    print(f'The {cipher_direction}d text is >>>>> {end_text} <<<<<')

go_again = 'yes'
while go_again == 'yes':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))


    caesar(start_text=text, shif_amount=shift, cipher_direction=direction)

    go_again = input('Type "yes" if you want to go again. Otherwise type "no"\n').lower()

print('Goodbye')




# ANOTHER WAY TO RUN THE CODE

# def encrypt(plain_text, shift_amount):
#     new_word = ''
#     for i in plain_text:
#         letter_pos = alphabet.index(i)
#         new_pos = letter_pos + shift_amount
#         if new_pos > 25:
#             new_letter = alphabet[new_pos-26]
#         else:
#             new_letter = alphabet[new_pos]
#         new_word += new_letter
#     print(f'The encode text is {new_word}')


# def decript(encrypt_text, shift_amount):
#     new_word = ''
#     for i in encrypt_text:
#         letter_pos = alphabet.index(i)
#         new_pos = letter_pos - shift_amount
#         if new_pos < 0:
#             new_letter = alphabet[26 + new_pos]
#         else:
#             new_letter = alphabet[new_pos]
#         new_word += new_letter
#     print(f'The decode text is {new_word}')

# if direction == 'encode':
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction =='decode':
#     decript(encrypt_text=text, shift_amount=shift)

