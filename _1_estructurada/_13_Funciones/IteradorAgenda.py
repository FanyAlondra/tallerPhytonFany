def extrae(agenda:tuple):
    i:int=0
    while(i<len(agenda)):
        nombre,correo,tel=agenda[i]
        i+=1
        yield nombre,correo, tel



if __name__ == '__main__':
    agenda=[]
    agenda.append(("juan","juan@mail.com","22258649012"))
    agenda.append(("juan1","juan1@mail.com","22258649013"))
    agenda.append(("juan2","juan2@mail.com","22258649014"))
    agenda.append(("juan3","juan3@mail.com","22258649015"))
    agenda.append(("juan4","juan4@mail.com","22258649016"))
    agenda.append(("juan5","juan5@mail.com","22258649017"))
    agenda.append(("juan6","juan6@mail.com","22258649018"))
    agenda.append(("juan7","juan7@mail.com","22258649019"))
    agenda.append(("juan8","juan8@mail.com","22258649011"))
    agenda.append(("juan9","juan9@mail.com","22258649021"))
    agenda.append(("juan10","juan10@mail.com","22258649022"))

    for a,b,c in extrae(agenda):
            print(f"valores: {a,b,c}")

