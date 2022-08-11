from caesar_cipher.is_english_word import check_confidence

def encrypt(plain, shift):

    def shift_upper(val):
        if val > 90:
            return (val - 90) + 64
        if val < 65:
            return  91 - (65 - val)
        return val

    def shift_lower(val):
        if val > 122:
            return (val - 122) + 96
        if val < 97:
            return  123 - (97 - val)
        return val

    encrypted = ""
    for char in plain:
        num = ord(char)
        if not 65 <= num <= 90 and not 97 <= num <= 122:
            encrypted += chr(num)
            continue

        shifted_num = num + (shift % 26)
        if 65 <= num <= 90:
            shifted_num = shift_upper(shifted_num)

        if 97 <= num <= 122:
            shifted_num = shift_lower(shifted_num)

        encrypted += chr(shifted_num)

    return encrypted

def decrypt(cipher, shift):
    return encrypt(cipher, -shift)

def crack(cipher):
    shift = 1
    while shift < 26:
        candidate = decrypt(cipher, shift)
        if check_confidence(candidate):
            return candidate
        shift += 1
    return ""