ALPHABET_RU="абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
ALPHABET_EN="abcdefghijklmnopqrstuvwxyz "
lang=input("Выберите язык ru/en: ").lower()
if lang=="ru":
   alphabet=ALPHABET_RU
elif lang=="en":
    alphabet=ALPHABET_EN
else:
    print("Язык не найден")
    exit()
message=input("Введите сообщение(без пробела):").lower()
cipher=[]
step=int(input("Введите шаг сдвига: "))
for symbol in message:
    index=alphabet.find(symbol) + step
    cipher.append(index)
print(cipher)
result=""
for number in cipher:
    result+=alphabet[number-step]
print(result)