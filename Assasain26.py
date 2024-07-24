def penis26():
 numbers = []
 print("Введите последовательность чисел, окончанием которой является 0:")

while True:
     num = int(input())
     if num == 0:
        break
        numbers.append(num)

negative = False

for i in range(len(numbers)):
    if negative:
        print("Первое число после первого отрицательного:", numbers[i])
        continue
    if numbers[i] < 0:
         negative = True

print("Отрицательных чисел не было в последовательности.")

