def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            if 'a' <= char <= 'z':
                shifted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            else:
                shifted_char = char
            if is_upper:
                shifted_char = shifted_char.upper()
            encrypted_text += shifted_char
        else:
            encrypted_text += char
    return encrypted_text

def main():
    while True:
        action = input("Введіть '1' для шифрування або '2' для розшифрування (або '3' для виходу): ")
        if action == '3':
            break

        if action != '1' and action != '2':
            print("Введіть '1' або '2' для вибору опції.")
            continue

        input_option = input("Введіть '4' для роботи з файлом або '5' для введення тексту: ")
        if input_option != '4' and input_option != '5':
            print("Введіть '4' або '5' для вибору опції.")
            continue

        if input_option == '5':
            input_text = input("Введіть текст: ")
        else:
            file_name = input("Введіть ім'я файлу: ")
            with open(file_name, 'r', encoding='utf-8') as file:
                input_text = file.read()

        shift = int(input("Введіть ключ для шифру Цезаря: "))
        output_file = input("Введіть ім'я файлу для збереження результату (наприклад, result.txt): ")

        if action == '1':
            encrypted_text = caesar_cipher(input_text, shift)
            with open(output_file, 'w', encoding='utf-8') as file:
                file.write(encrypted_text)
            print(f"Текст зашифровано та збережено у файлі {output_file}.")
        else:
            decrypted_text = caesar_cipher(input_text, -shift)
            with open(output_file, 'w', encoding='utf-8') as file:
                file.write(decrypted_text)
            print(f"Текст розшифровано та збережено у файлі {output_file}.")

if __name__ == '__main__':
    main()
