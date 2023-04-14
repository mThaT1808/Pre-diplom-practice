def ThirdTask():
    print(
        "Дан список строк.\n",
        "Нужно вывести все буквы, которые встречаются в каждой из строк списка\n",
        "(включая дубли).\n",
        "\n",
        "Example\n",
        '["bella","label","roller"] -> ["e","l","l"] ["cool","lock","cook"] -> ["c","o"]\n'
    )

    lst =  ["cool","lock","cook"]

    def split(s):
        return [char for char in s]



    def same_elements(a, b):
        repeated = []
        for i in range(len(a)):
            for j in range(len(b)):
                if a[i] == b[j]:
                    repeated.append(a[i])
                    b.pop((j))
                    break
        return repeated
    repeated = split(lst[0])



    for i in range(len(lst)):
        repeated = same_elements(repeated, split(lst[i]))

    print(repeated)













