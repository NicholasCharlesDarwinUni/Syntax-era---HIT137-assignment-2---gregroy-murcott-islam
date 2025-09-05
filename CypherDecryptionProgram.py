modetype = input("encrypt or Decrytpt?  ")
example = str(input("encrypt me  "))
shiftvalue1 = int(input("input shift value 1 "))
shiftvalue2 = int(input("input shift value 2 "))
number = "​"
result = ""


i = 0

if modetype == 'decrypt':
    while i < len(example):
        if example[i] == "​":
            i += 1  # Move to the character after '*'
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