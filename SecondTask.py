import random


def SecondTask():
    print(
        "отсортировать 1й список по элементам 2го\n",
        "дан массив a = [1, 4, 6] и массив  b = [11, 33, 22]\n",
        "если отсортировать первый массив по второму должен получиться массив [1,6,4]\n"
    )
    A = []
    B = []

    for i in range(3):
        A.append(int(random.uniform(0, 100)))
        B.append(int(random.uniform(0, 100)))

    print("Первоначальный массив А: ", A,
          "\nПервоначальный массив B: ", B
          )
    for j in range(len (B)):
        for i in range(len(B)):
            if i >= 1:
                if (B[i] < B[i - 1]):
                    a = A[i]
                    A[i] = A[i - 1]
                    A[i - 1] = a
                    b = B[i]
                    B[i] = B[i - 1]
                    B[i - 1] = b
    print("Массив после сортировки А: ", A,
          "\nМассив после сортировки B: ", B
          )
