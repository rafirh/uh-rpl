def soal_1():  
    print("========== 1. Mana yang lebih besar ? ==========")  
    arr = []
    n = int(input("Enter number of digits : "))
    for i in range(0, n):
        element = int(input("Enter digit [" + str(i + 1) + "] : "))
        arr.append(element)
    print("Result : " + str(max(arr)))

def soal_2():  
    print("========== 2. Ganjil atau genap ==========")  
    arr = []
    n = int(input("Enter number : "))
    result = ""
    if (n % 2 == 0):
        result = "Genap";
    else:
        result = "Ganjil";
    print(result)

def soal_3():  
    print("========== 2. Berapakah jumlahnya ? (jumlah dari 1 sampai ke n) ==========")  
    arr = []
    n = int(input("Enter number : "))
    result = 0
    for i in range(1, n + 1):
        result += i;
    print(result)

def soal_4():  
    print("========== 4. Ganjil atau genap chapter 2 ==========")  
    arr = []
    n = int(input("Enter number of array : "))
    for i in range(0, n):
        element = int(input("Enter array element [" + str(i) + "] : "))
        arr.append(element)
    result = []
    for i in arr:
        if (i % 2 == 0):
            result.append("genap")
        else:
            result.append("ganjil")
    print(result)

def soal_5():  
    print("========== 5. Nilai Maksimun ? ==========")  
    arr = []
    n = int(input("Enter number of array : "))
    for i in range(0, n):
        element = int(input("Enter array element[" + str(i + 1) + "] : "))
        arr.append(element)
    print("Result : " + str(max(arr)))

def soal_6():  
    print("========== 6. Mungkinkah ? ==========")  
    arr = []
    n = int(input("Enter number of array : "))
    k = int(input("Enter number of K : "))
    result = 0
    for i in range(0, n):
        element = int(input("Enter array element [" + str(i) + "] : "))
        arr.append(element)
    for i in range(0, n):
        for j in range(0, n):
            if(i != j):
                if(arr[i] + arr[j] == k):
                    result += 1
    result2 = "" 
    if(result > 0):
        result2 = "BISA"
    else:
        result2 = "TIDAK BISA"
    print("Result : " + result2)

def soal_7():  
    print("========== 7. Apakah semua berbeda ? ==========")  
    arr = []
    n = int(input("Enter number of array : "))
    result = 0
    for i in range(0, n):
        element = int(input("Enter array element [" + str(i) + "] : "))
        arr.append(element)
    for i in range(0, n):
        for j in range(0, n):
            if(i != j):
                if(arr[i] == arr[j]):
                    result += 1
    result2 = "" 
    if(result > 0):
        result2 = "ADA"
    else:
        result2 = "TIDAK ADA"
    print("Result : " + result2 + " YANG SAMA")

def soal_8():  
    print("========== 8. Penjualan buah ==========")  
    fruits = []
    sumFruits = []
    n = int(input("Enter number of fruits : "))
    for i in range(0, n):
        fruit = input("Enter fruit[" + str(i) + "] : ")
        sumFruit = int(input("Enter sum[" + str(i) + "] : "))
        fruits.append(fruit)
        sumFruits.append(sumFruit)
    maxSum = max(sumFruits);
    print("Result : " + fruits[sumFruits.index(maxSum)])

question = int(input("Enter number of question (1 - 8) : "))
if(question == 1):
    soal_1()
elif(question == 2):
    soal_2()
elif(question == 3):
    soal_3()
elif(question == 4):
    soal_4()
elif(question == 5):
    soal_5()
elif(question == 6):
    soal_6()
elif(question == 7):
    soal_7()
elif(question == 8):
    soal_8()
else:
    print("Question not found ...")
