password = input("Enter your password: ")
l = []
for letter in password:
    a = letter

    b = (ord(a[0]))

    c = (b+1)

    char = chr(c)
    l.append(char)

x = "".join(l)

print("Encrypted Password is: ", x)
print(password.len())









