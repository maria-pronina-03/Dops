N=int(input("Введите кол-во элементов массива: ")) #задание размерности массива
A = [0]*N  #создание массива
for i in range(N):
    A[i] = int( input("Введите элементы массива: ") )
print ("Массив: ", A)
sr=0;
sr=sum(A)//N #считаем среднее значение массива
kol=0;
for i in range(N):
    if A[i]>sr: #если элемент больше сренего значения
        kol=kol+1 #то увеличиваем счетчик на 1
print("Среднее значение массива: ", sr)
print("Количество элементов в массиве, которые больше ср значения", kol)
