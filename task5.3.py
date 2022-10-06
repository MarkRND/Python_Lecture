# Напишите программу, удаляющую из текста все слова, содержащие "абв".





text = 'абв абвгд гдеёжз непшщтг'
text =list(filter(lambda i: not'абв' in i, text.split()))
print(text)