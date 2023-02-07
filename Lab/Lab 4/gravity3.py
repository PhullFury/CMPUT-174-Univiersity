english_capital = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
english_small = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26']

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

def decrypt_atbash(word):
    decrypt_list = []
    for char in word:
        if (char in english_capital):
            index = english_capital.index(char)
            shift_index = index - 25
            if (shift_index < 0):
                shift_index = -shift_index
            decrypt_list.append((english_capital[shift_index]))
        elif (char in english_small):
            index = english_small.index(char)
            shift_index = index - 25
            if (shift_index < 0):
                shift_index = -shift_index
            decrypt_list.append((english_small[shift_index]))
        else:
            decrypt_list.append(char)
    return "".join(decrypt_list)

def decrypt_a1z26(word):
    temp_list = []
    temp_word = ""
    temp_list2 = []
    for i in word:
        if (i.isnumeric()):
            temp_list.append(i)
        elif (i == "-"):
            temp_word = "".join(temp_list)
            temp_list2.append(temp_word)
            temp_list = []
        else:
            temp_word = "".join(temp_list)
            temp_list2.append(temp_word)
            temp_list2.append(i)
            temp_list = []

    decrypt_list = []
    for i in temp_list2:
        if (i in numbers):
            index = numbers.index(i)
            decrypt_list.append(english_capital[index])
        else:
            decrypt_list.append(i)
    return "".join(decrypt_list)

def main():
    word = input("Write a word: ") + " "
    shift = int(input("Write the shift value: "))

    print("\nLet's try all the methods we have:")
    print("Cypher cipher: " + decrypt_caesar(word, shift))
    print("Atbash cipher: " + decrypt_atbash(word))
    print("A1Z26 cipher: " + decrypt_a1z26(word))

main()