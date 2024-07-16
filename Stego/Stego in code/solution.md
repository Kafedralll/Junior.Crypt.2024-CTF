Открываем файл в Notepad++. <br>
Режим "Вид" - "Отображение символов" - "Отображать все символы" 

<p align="center">
 <img width="300px" src="../../img/StegoInCode-01.png" alt="qr"/>
</p>
<!--![Image alt](https://github.com/Kafedralll/Junior.Crypt.2024-CTF/blob/main/img/StegoInCode-01.png)-->

Гипотеза: Сообщение скрыто с использованием кодировки CR/LF и LF/CR.

# Пишем скрипт для извлечения сообщения
fi = open("StegoInCode.py", 'rb').read()
stego = ""
ib = 0
while ib < len(fi)-1:
    if fi[ib:ib+2] == b'\x0a\x0d':  # CR/LF
        stego += '0'
        ib += 2
    elif fi[ib:ib+2] == b'\x0d\x0a': # LF/CR
        stego += '1'
        ib += 2
    else:
        ib += 1
# Получили битовую строку        
print (stego)
print ()
# Переводим ее в ASCII и видим флаг
print ("".join([chr(int(stego[i:i+8],2)) for i in range(0, len(stego), 8)]))

ÿÿÿgrodno{stego_vs_cryptography}ÿÿÿÿÿÿÿ?
