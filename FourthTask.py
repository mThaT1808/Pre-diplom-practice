def FourthTask():
    print("Дана римская цифра, преобразовать ее в целое число.")

    def split(s):
        return [char for char in s]

    def get_arabic_numbers(t):
        l = list()

        format = 0

        for i in range(0, len(t)):
            if t[i] == 'I':
                l.append(int(1))
            elif t[i] == 'V':
                l.append(int(5))
            elif t[i] == 'X':
                l.append(int(10))
            elif t[i] == 'L':
                l.append(int(50))
            elif t[i] == 'C':
                l.append(int(100))
            elif t[i] == 'D':
                l.append(int(500))
            elif t[i] == 'M':
                l.append(int(1000))

        i = 0
        while i < len(l) - 1:
            if l[i] < l[i + 1]:
                format = format + l[i + 1] - l[i];
                i = i + 2
            else:
                format = format + l[i]
                i = i + 1

        return format

    rom_number = 'MCDLVI'
    splitted_rom = split(rom_number)

    arabic_number = get_arabic_numbers(splitted_rom)
    print(rom_number, '- Римское число\n', arabic_number, '- Арабское число\n')

