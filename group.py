def groups_of_three(lista:list[int])->list[list[int]]:
    listb = []
    new = []
    for i in range(len(lista)):
        if len(new) == 3:
            listb.append(new)
            new = []
        new.append(lista[i])
        if i == len(lista)-1:
            listb.append(new)
    return listb