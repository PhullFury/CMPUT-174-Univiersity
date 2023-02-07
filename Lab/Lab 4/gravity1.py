english_capital = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
english_small = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def decrypt_caesar(word, shift):
    decrypt_list = []
    for char in word:
        if (char in english_capital):
            index = english_capital.index(char)
            shift_index = index - shift
            if (shift_index < 0):
                shift_index += 26
            decrypt_list.append(english_capital[shift_index])
        elif (char in english_small):
            index = english_small.index(char)
            shift_index = index - shift
            if (shift_index < 0):
                shift_index += 26
            decrypt_list.append(english_small[shift_index])
        else:
            decrypt_list.append(char)
    return "".join(decrypt_list)

def main():
    word = input("Write a word: ") + " "
    shift = int(input("Write the shift value: "))

    print("Decryption: " + decrypt_caesar(word, shift))

main()