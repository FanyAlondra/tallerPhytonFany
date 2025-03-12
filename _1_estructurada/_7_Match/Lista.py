import sys
if __name__ == '__main__':
    lista=[1,2,5,1,5,4,9,1,4,70,0,2,1,9,7,10,1,4,3,30,1,5,-1,3,9,7,1,10]
    totales = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    adoptados: int = 0

    for elemento in lista:

        match elemento:
            case 1:totales[0]+=1
            case 2:totales[1]+=1
            case 3:totales[2] += 1
            case 4: totales[3] += 1
            case 5: totales[4] += 1
            case 6: totales[5] += 1
            case 7: totales[6] += 1
            case 8:totales[7] += 1
            case 9: totales[8] += 1
            case 10: totales[8] += 1
            case _: adoptados += 1
    i:int=1
    for n in totales:
        print(f"{i}.-{n}")
        i+=1


