import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

tablica_hasła = []

print("Generator hasel!")
nr_letters = int(input("Ile liter chcesz w swoim haśle?\n"))
nr_symbols = int(input(f"Ile symboli chcesz?\n"))
nr_numbers = int(input(f"Ile liczb chcesz?\n"))

password = ""
for i in range(0, nr_letters):
    randomek_letters = random.randint(0, len(letters) - 1)
    tablica_hasła += letters[randomek_letters]

for i in range(0, nr_symbols):
    randomek_symbols = random.randint(0, len(symbols) - 1)
    tablica_hasła += symbols[randomek_symbols]

for i in range(0, nr_numbers):
    randomek_numbers = random.randint(0, len(numbers) - 1)
    tablica_hasła += numbers[randomek_numbers]

print(tablica_hasła)
print(len(tablica_hasła))

# kazdy obrot petli losuje w tablicy element, pozniej go dodaje na koniec tablicy hasla

for obroty in range(0, len(tablica_hasła)):
    los_tablica = random.randint(0, len(tablica_hasła) - 1)
    print("losuje element w tablicy nr :", los_tablica)
    password += tablica_hasła[los_tablica]

    print("dodaje do hasła wylosowany element:", password)
    print("usuwam element:", tablica_hasła[los_tablica])
    del tablica_hasła[los_tablica]

    print(tablica_hasła)
    print("---------------------------")
print("Twoje wygenerowane haslo to: " + password)
