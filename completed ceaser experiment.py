modetype = input("encrypt or decrytpt?  ")
example = str(input("encrypt me  "))
shiftvalue1 = int(input("input shift value 1 "))
shiftvalue2 = int(input("input shift value 2 "))
number = "​"
result = ""

i = 0

if modetype == 'encrypt':
    for char in example:
        if 'a' <= char <= 'm':
            start = ord('a')
            shifted_char_code = (ord(char) - start + (shiftvalue1 * shiftvalue2)) % 26 + start
            result += chr(shifted_char_code)
        elif 'n' <= char <= 'z':
            start = ord('a')
            shifted_char_code = (ord(char) - start - (shiftvalue1 + shiftvalue2)) % 26 + start
            result += number
            result += chr(shifted_char_code)
        elif 'A' <= char <= 'M':
            start = ord('A')
            shifted_char_code = (ord(char) - start - shiftvalue1) % 26 + start
            result += chr(shifted_char_code)
        elif 'N' <= char <= 'Z':
            start = ord('A')
            shifted_char_code = (ord(char) - start + (shiftvalue2 * shiftvalue2)) % 26 + start
            result += number
            result += chr(shifted_char_code)
        elif char < 'A' or char > 'z':
            result += char
elif modetype == 'decrypt':
    while i < len(example):
        if example[i] == "​":
            i += 1 
            if i < len(example):
                char = example[i]
                if char.islower():
                    start2 = ord('a')
                    exciting_variable = (ord(char) - start2 + (shiftvalue1 + shiftvalue2)) % 26 + start2
                    result += chr(exciting_variable)
                elif char.isupper():
                    start = ord('A')
                    exciting_variable = (ord(char) - start - (shiftvalue2 * shiftvalue2)) % 26 + start
                    result += chr(exciting_variable)
        else:
            char = example[i]
            if char.islower():
                start2 = ord('a')
                exciting_variable = (ord(char) - start2 - (shiftvalue1 * shiftvalue2)) % 26 + start2
                result += chr(exciting_variable)
            elif char.isupper():
                start = ord('A')
                exciting_variable = (ord(char) - start + shiftvalue1) % 26 + start
                result += chr(exciting_variable)
            else:
                result += char
        i += 1

print(result)



