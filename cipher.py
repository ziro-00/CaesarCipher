def encrypt(text, shift):

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    fText = ''
    for i in text:
        if i.lower() in alphabet:
            position = (alphabet.index(i) + shift) % 26
            if i.isupper():
                fText += alphabet[position].upper()
            else:
                fText += alphabet[position]  
        else:
            fText += i
    return fText

def bruteforce(text):
    
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    results = {}

    for shift in range(0, 26):
        result = ''

        for char in text:
            if char.lower() in alphabet:
                position = (alphabet.index(char.lower()) + shift) % 26
                if char.isupper():
                    result += alphabet[position].upper()
                else:
                    result += alphabet[position]
            else:
                result += char

        results[shift] = result

    return results


def decrypt(text, shift):
    return encrypt(text, -shift)