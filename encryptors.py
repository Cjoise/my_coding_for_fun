# This is a program comprising different encryptors.

#Cell phone numbers encryptor:

def cellphone_keys():
    cellboard = {'0': ' ', '1': '.,?!:', '2': 'ABC', '3': 'DEF', '4': 'GHI', '5': 'JKL', '6': 'MNO', '7': 'PQRS', '8': 'TUV', '9': 'WXYZ'}
    result = ''
    values = list(cellboard.values())
    keys = list(cellboard.keys())
    text = input('Enter text in English to encrypt: ').upper()
    for c in text:
        if c in ''.join(values):
            for i in range(len(values)):
                for j in range(len(values[i])):
                    if values[i][j] == c:
                        result += f'[{keys[i] * (j + 1)}]'
        elif c.isdigit():
            result += f'[{c}]'
        else:
            result += '[ ]'
    return result

#Morse encryptor:

def morse_enc():
    import string as s
    chrs = s.ascii_uppercase + s.digits
    morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.']
    transfer = dict(zip(chrs, morse))
    text = input('Enter text in English to encrypt: ').upper()
    result = ''
    for c in text:
        if c in chrs:
            result += transfer[c] + ' '
        else:
            result += ' '
    return result

#Russian letters into English letters transliteration:

def translit():
    rus = list("абвгдеёжзийклмнопрстуфхцчшщъыьэюя")
    eng = "a-b-v-g-d-je-jo-zh-z-i-j-k-l-m-n-o-p-r-s-t-u-f-h-c-ch-sh-sch-'-y-'-e-ju-ja".split('-')
    alphabet = dict(zip(rus, eng))
    rus_text = input('Enter text in Russian to encrypt: ')
    for c in rus_text:
        if c.lower() in alphabet:
            if c.isupper():
                rus_text = rus_text.replace(c.upper(), alphabet[c.lower()].title())
            else:
                rus_text = rus_text.replace(c, alphabet[c])
    return rus_text

#Words censorship encryptor:

def word_cleaner():
    text = input('Enter text to process: ')
    forbidden_words = input('Enter forbidden words divided by space: ')
    text_copy = text.lower()
    fw = forbidden_words.lower().split()
    for word in fw:
        while word in text_copy:
            text = text.replace(text[text_copy.index(word):text_copy.index(word) + len(word)], '*' * len(word), -1)
            text_copy = text.lower()
    text = list(map(lambda x: '[censured]' if '*' in x else x, text.split()))
    return ' '.join(text)

# Body of the program:

dct = {'A': 'English words into cell-phone numbers', 'B': 'English words into morse', 'C': 'Russian words into English transliteration', 'D': 'To apply censorship to any forbidden words'}
print('Welcome to the encryptor!', 'Please choose what you want to encrypt:', f'A - {dct["A"]}', f'B - {dct["B"]}', f'C - {dct["C"]}', f'D - {dct["D"]}', sep='\n')
commands = {'A': cellphone_keys, 'B': morse_enc, 'C': translit, 'D': word_cleaner}
while True:
    answer = input('Please press keys A, B, C or D to choose an encryptor or Q to quit:  ').upper()
    if answer in commands:
        print(f'You have chosen [{answer}][{dct[answer]}]')
        if answer in dct:
            print('The result is: ', commands[answer]())
            again = input('Start again? [Press Y for continue or any other key to quit]: ').lower()
            if again == 'y':
                continue
            else:
                print("Exiting...", "Exited.", sep='\n')
                break
    elif answer == 'q'.upper():
        print("You pressed Q. Exiting...", "Exited.", sep='\n')
        break
    else:
        print('Please try again.')
        continue
