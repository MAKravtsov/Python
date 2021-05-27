# Введите количество изделий
print ('Количество изделий')
productCnt=int(input())

# Количество рабочих мест на конвейере
print ('Количество рабочих мест')
workPlacesCnt=int(input())

# Время механообработки
print ('Время механообработки партии')
machiningTime=float(input())

# Заполняем время сборки каждого типа деталей
assemblyTimesForDetails=[]
print('Время сборки каждой детали в изделие')
for i in range (workPlacesCnt):
    assemblyTimesForDetails.append(float(input()))

# Общее время сборки
assemblyTime=0
# Расчет общего времени сборки
if productCnt<=workPlacesCnt:
    for i in range(1, productCnt+workPlacesCnt):
        if i<=productCnt:
            assemblyTime += max(assemblyTimesForDetails[0:i])
        elif i>workPlacesCnt:
            assemblyTime += max(assemblyTimesForDetails[(i-productCnt):workPlacesCnt])
        else :
            assemblyTime += max(assemblyTimesForDetails[(i - productCnt):i])
else:
    for i in range(1, productCnt+workPlacesCnt):
        if i<=workPlacesCnt:
            assemblyTime += max(assemblyTimesForDetails[0:i])
        elif i>productCnt:
            assemblyTime += max(assemblyTimesForDetails[(i-productCnt):workPlacesCnt])
        else :
            assemblyTime += max(assemblyTimesForDetails[0:workPlacesCnt])

# Вывод результатов
print ('Общее время сборки =',assemblyTime)
if ((assemblyTime<machiningTime) and (abs(((machiningTime-assemblyTime)/machiningTime)*100)<=5)):
    print('Механообрабатывающий цех и сборочный согласованы\n',
         'Попробуйте уменьшить количество мест на конвейере в ', machiningTime/assemblyTime,' раз')
elif ((assemblyTime>=machiningTime) and (abs(((assemblyTime-machiningTime)/machiningTime)*100)<=5)):
    print ('Механообрабатывающий цех и сборочный согласованы')
else:
    print ('Механообрабатывающий цех и сборочный НЕ согласованы! Уменьшите время обработки деталей')