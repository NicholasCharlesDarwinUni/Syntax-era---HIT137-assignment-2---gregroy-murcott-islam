modetype = input("encrypt or Decrytpt?  ")
example = str(input("encrypt me  "))
shiftvalue1 = int(input("input shift value 1 "))
shiftvalue2 = int(input("input shift value 2 "))

result = ""
if modetype == 'encrypt':
    for char in example:
        if 'a' <= char <= 'm':
            start = ord('a')
            shifted_char_code = (ord(char) - start + (shiftvalue1 * shiftvalue2)) % 26 + start
            result += chr(shifted_char_code)
        elif 'n' <= char <= 'z':
            start = ord('a')
            shifted_char_code = (ord(char) - start - (shiftvalue1 + shiftvalue2)) % 26 + start
            result += chr(shifted_char_code)
        elif 'A' <= char <= 'M':
            start = ord('A')
            shifted_char_code = (ord(char) - start - shiftvalue1) % 26 + start
            result += chr(shifted_char_code)
        elif 'N' <= char <= 'Z':
            start = ord('A')
            shifted_char_code = (ord(char) - start + (shiftvalue2 * shiftvalue2)) % 26 + start
            result += chr(shifted_char_code)
        elif char < 'A' or char > 'z':
            result += char
elif modetype == 'decrypt':
    for char in example:
        if char.islower():
            start = ord('a')
            shifted_char_code = (ord(char) - start - (shiftvalue1 * shiftvalue2)) % 26 + start
            if 97 <= shifted_char_code <= 109: 
                start2 = ord('a')
                exciting_variable = (ord(char) - start2 - (shiftvalue1 * shiftvalue2)) % 26 + start
                result += chr(exciting_variable)
            else:
                start2 = ord('a')
                exciting_variable = (ord(char) - start2 + (shiftvalue1 + shiftvalue2)) % 26 + start
                result += chr(exciting_variable)
        elif char.isupper():
            start = ord('A')
            shifted_char_code = (ord(char) - start + shiftvalue1) % 26 + start
            if 65 <= shifted_char_code <= 77:
                start = ord('A')
                exciting_variable = (ord(char) - start + shiftvalue1) % 26 + start
                result += chr(exciting_variable)
            else:
                start = ord('A')
                exciting_variable = (ord(char) - start - (shiftvalue2 * shiftvalue2)) % 26 + start
                result += chr(exciting_variable)
        elif char < 'A' or char > 'z':
            result += char



print(result)