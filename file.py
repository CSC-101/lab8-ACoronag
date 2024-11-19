def file_reader(file):
    try:
        file = open(file)
    except FileNotFoundError:
        exit()
    for line in file:
        split = line.split()
        temp_list = []
        for value in split:
            try:
                num = float(value)
                temp_list.append(num)
            except ValueError:
                print("One of the values couldn't be converted")
        sum = 0
        if len(temp_list) != 2:
            print("not enough terms")
        else:
            for i in range(len(temp_list)):
                sum += temp_list[i]
            print(sum)


file_reader("txt.txt")