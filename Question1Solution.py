shiftvalue1 = int(input("Input shift value 1: "))
shiftvalue2 = int(input("Input shift value 2: "))
number = "​"  

with open("raw_text.txt", "r", encoding="utf-8") as file:
    example = file.read()

result = ""

for char in example:
    if char == '\n':
        result += char
        continue
    if 'a' <= char <= 'm':
        start = ord('a')
        shifted_char_code = (ord(char) - start + (shiftvalue1 * shiftvalue2)) % 26 + start
        result += chr(shifted_char_code)
    elif 'n' <= char <= 'z':
        start = ord('a')
        shifted_char_code = (ord(char) - start - (shiftvalue1 + shiftvalue2)) % 26 + start
        result += number + chr(shifted_char_code)
    elif 'A' <= char <= 'M':
        start = ord('A')
        shifted_char_code = (ord(char) - start - shiftvalue1) % 26 + start
        result += chr(shifted_char_code)
    elif 'N' <= char <= 'Z':
        start = ord('A')
        shifted_char_code = (ord(char) - start + (shiftvalue2 * shiftvalue2)) % 26 + start
        result += number + chr(shifted_char_code)
    else:
        result += char

print(result)

newexample = result
newresult = ""
i = 0
while i < len(newexample):
    if newexample[i] == number:
        i += 1
        if i < len(newexample):
            char = newexample[i]
            if char.islower():
                start2 = ord('a')
                exciting_variable = (ord(char) - start2 + (shiftvalue1 + shiftvalue2)) % 26 + start2
                newresult += chr(exciting_variable)
            elif char.isupper():
                start = ord('A')
                exciting_variable = (ord(char) - start - (shiftvalue2 * shiftvalue2)) % 26 + start
                newresult += chr(exciting_variable)
    else:
        char = newexample[i]
        if char.islower():
            start2 = ord('a')
            exciting_variable = (ord(char) - start2 - (shiftvalue1 * shiftvalue2)) % 26 + start2
            newresult += chr(exciting_variable)
        elif char.isupper():
            start = ord('A')
            exciting_variable = (ord(char) - start + shiftvalue1) % 26 + start
            newresult += chr(exciting_variable)
        else:
            newresult += char
    i += 1

newresult = newresult.replace(number, '')
print(newresult)
with open("decrypted_text.txt", "w", encoding="utf-8") as newtextfile:
    newtextfile.write(newresult)




with open("raw_text.txt", 'r', encoding='utf-8') as start, \
        open("decrypted_text.txt", 'r', encoding='utf-8') as finish:
    
    file1 = start.read()
    file2 = finish.read()

    if file1 == file2:
        print("These files are the same.")
    else:
        print("These files are not the same.")

