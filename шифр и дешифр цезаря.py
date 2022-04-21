# ввод данных
encryption_or_decryption = input('Выберите: ш = шифрование или д = дешифрование: ')
ru_or_en = input('Выберите язык р = русский или а = английский: ')
shift_step = int(input('Выберите шаг шифрования от 1 до 31: '))
text = list(input('Введите текст для шифрования/дешифрования: \n'))

if encryption_or_decryption == 'д' and ru_or_en == 'р':
    shift_step = 32 - shift_step
elif encryption_or_decryption == 'д' and ru_or_en == 'а':
    shift_step = 26 - shift_step

if ru_or_en == 'р':  # шифрование русского текста
    for i in range(len(text)):
        if text[i].isalpha() and text[i].isupper() and ord(text[i]) + shift_step <= ord('Я'):
            text[i] = chr(ord(text[i]) + shift_step)
        elif text[i].isalpha() and text[i].isupper() and ord(text[i]) + shift_step > ord('Я'):
            text[i] = chr(ord(text[i]) + shift_step - ord('Я') + ord('А') - 1)
        elif text[i].isalpha() and text[i].islower() and ord(text[i]) + shift_step <= ord('я'):
            text[i] = chr(ord(text[i]) + shift_step)
        elif text[i].isalpha() and text[i].islower() and ord(text[i]) + shift_step > ord('я'):
            text[i] = chr(ord(text[i]) + shift_step - ord('я') + ord('а') - 1)

elif ru_or_en == 'а':  # шифрование английского текста
    for i in range(len(text)):
        if text[i].isalpha() and text[i].isupper() and ord(text[i]) + shift_step <= ord('Z'):
            text[i] = chr(ord(text[i]) + shift_step)
        elif text[i].isalpha() and text[i].isupper() and ord(text[i]) + shift_step > ord('Z'):
            text[i] = chr(ord(text[i]) + shift_step - ord('Z') + ord('A') - 1)
        elif text[i].isalpha() and text[i].islower() and ord(text[i]) + shift_step <= ord('z'):
            text[i] = chr(ord(text[i]) + shift_step)
        elif text[i].isalpha() and text[i].islower() and ord(text[i]) + shift_step > ord('z'):
            text[i] = chr(ord(text[i]) + shift_step - ord('z') + ord('a') - 1)

print(*text, sep='')