import random
import string

lenght = int(input("Enter the password length: "))

include_digits = input("Include digits? (Y/N): ").upper()
include_punctuatuion = input("Include punctuation? (Y/N): ").upper()

chars = string.ascii_letters

if include_digits == "Y":
    chars += string.digits

if include_punctuatuion == "Y":
    chars += string.punctuation

password1 = "".join(random.choices(chars, k=lenght))
password2 = "".join(random.choices(chars, k=lenght))
password3 = "".join(random.choices(chars, k=lenght))

print("Generate password: ", password1)
print("Generate password: ", password2)
print("Generate password: ", password3)

with open ("generated_passwords.txt", "w") as file:
    file.write("Generated passwords:\n")
    file.write(password1 + "\n")
    file.write(password2 + "\n")
    file.write(password3 + "\n")
    
print("Пароли сохранены в файл generated_passwords.txt")