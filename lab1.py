x=int (input("Введите число в диапазоне от 1 до 9: "))
if (x>=1) and(x<=3):
    s=input("Введите строку: ")
    n= int("Введите количество повторов строки: ")
    i=1
    while i<=n:
        print(s)
        i+=1
elif(x>=4) and (x<=6):
    m=int("Введите степень в которую хотите возвести число: ")
    print(pow(x,m))
elif (x>=7) and (x<=9):
    j=1
    while j<10:
        x+=1
        print(x)
        j+=1
    else:
        print("Ошибка ввода !")

