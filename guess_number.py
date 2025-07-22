import random

surprise = random.randint(1, 10)
player = int(input("Insert number from 1 to 10: "))
attempts = 1

while player != surprise:
    
    if player < surprise:
        print ("Too low!")

    elif player > surprise:
        print ("Too high!")

    player = int(input("Try again: "))
    attempts += 1

print("You`re lucky!")
print(f"Ты угадал с {attempts} попытки!")
