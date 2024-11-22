number = int(input('Введите трехзначное число'))

last = number%10

other = number//10

chislo = last*100+other

print(chislo)