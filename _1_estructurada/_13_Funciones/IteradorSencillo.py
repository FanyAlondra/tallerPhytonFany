def ciclos(vueltas:int):
    i:int=0
    while(i<vueltas):
        i+=1
        yield i
    return i



if __name__ == '__main__':
    for valor in ciclos(50):
        print(valor)
    #valor=vueltas=(20)
    #print(f"vueltas:" {valor})