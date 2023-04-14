def FirstTask():
    print(
        "FizzBuzz\n ",
        "перебрать числа от 1 до 100\n",
        "если число делится на 3 - вывести вместо него Fizz\n",
        "если на 5 - вывести вместо него Buzz\n",
        "если и на 3 и на 5 - вывести вместо него FizzBuzz\n"
    )
    for i in range(100):
        if i % 3 == 0:
            if i % 5 == 0:
                print("FizzBuzz")
            else:
                print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)