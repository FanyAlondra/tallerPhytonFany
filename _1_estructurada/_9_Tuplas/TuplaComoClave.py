if __name__ == '__main__':
    diccionario={}
     #   'id':'2',
      #  'nombre':'juan',
       # 'apellido':'gutierrez'


    #agrgar tupla con clave

    diccionario[("ana",25)] = "estudiante"
    diccionario[("luis", 30)] = "ingeniero"
    diccionario[("carlos", 40)] = "abogado"

    #acceder a los valores del diccionario usando la tupla
    ocupacion_ana = diccionario[("ana",25)]
    ocupacion_luis = diccionario[("luis", 30)]

    print(f"ana es: {ocupacion_ana}")
    print(f"luis es: {ocupacion_luis}")
