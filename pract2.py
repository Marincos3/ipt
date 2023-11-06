
def generate_key(keyword, text_length):
    keyword = keyword.lower()
    key = ""
    keyword_index = 0
    for char in range(text_length):
        if keyword_index == len(keyword):
            keyword_index = 0
        key += keyword[keyword_index]
        keyword_index += 1
    return key


def vigenere_encrypt(text, keyword):
    encrypted_text = ""
    for i in range(len(text)):
        if text[i] == ' ':
            encrypted_text += ' '
        else:
            text_char = ord(text[i]) - 1072
            keyword_char = ord(keyword[i]) - 1072
            encrypted_char = (text_char + keyword_char) % 33
            encrypted_text += chr(encrypted_char + 1072)

    return encrypted_text


def vigenere_decrypt(encrypted_text, keyword):
    decrypted_text = ""
    for i in range(len(encrypted_text)):
        if encrypted_text[i] == ' ':
            decrypted_text += ' '
        else:
            encrypted_char = ord(encrypted_text[i]) - 1072
            keyword_char = ord(keyword[i]) - 1072
            decrypted_char = (encrypted_char - keyword_char) % 33
            decrypted_text += chr(decrypted_char + 1072)

    return decrypted_text


def save_to_file(filename, text):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)


def read_from_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()

while True:
    action = input("Виберіть опцію (1 - Шифрувати, 2 - Дешифрувати, 3 - Вийти): ")

    if action == '1':

        source_choice = input("Виберіть джерело тексту (1 - Ввести текст, 2 - Вибрати файл): ")

        if source_choice == '1':
            plaintext = input("Введіть текст для шифрування (український текст): ")
        elif source_choice == '2':
            file_name = input("Введіть назву файлу, який потрібно зашифрувати: ")
            plaintext = read_from_file(file_name)
        else:
            print("Невірний вибір для джерела тексту.")
            continue

        student_name = input("Введіть ім'я студента (ключове слово для шифрування): ")
        key = generate_key(student_name, len(plaintext))
        encrypted_text = vigenere_encrypt(plaintext, key)

        output_file = input("Введіть назву файлу для збереження зашифрованого тексту (з розширенням .txt): ")
        save_to_file(output_file, encrypted_text)
        print(f"Зашифрований текст збережено у файлі {output_file}")

    elif action == '2':

        key_choice = input("Виберіть спосіб введення ключа (1 - Ввести ключ, 2 - Вибрати файл із ключем): ")

        if key_choice == '1':
            student_name = input("Введіть ім'я студента (ключ для дешифрування): ")
        elif key_choice == '2':
            key_file_name = input("Введіть назву файлу, який містить ключ: ")
            student_name = read_from_file(key_file_name)
        else:
            print("Невірний вибір для ключа.")
            continue


        source_choice = input("Виберіть джерело зашифрованого тексту (1 - Ввести текст, 2 - Вибрати файл): ")

        if source_choice == '1':
            encrypted_text = input("Введіть зашифрований текст: ")
        elif source_choice == '2':
            file_name = input("Введіть назву файлу з зашифрованим текстом: ")
            encrypted_text = read_from_file(file_name)
        else:
            print("Невірний вибір для джерела тексту.")
            continue

        key = generate_key(student_name, len(encrypted_text))
        decrypted_text = vigenere_decrypt(encrypted_text, key)

        output_file = input("Введіть назву файлу для збереження дешифрованого тексту (з розширенням .txt): ")
        save_to_file(output_file, decrypted_text)
        print(f"Дешифрований текст збережено у файлі {output_file}")

    elif action == '3':
        break
    else:
        print("Невірний вибір. Виберіть опцію 1, 2 або 3.")
