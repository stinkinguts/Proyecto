# -*- coding: utf-8 -*-
"""
Created on Tue May 24 09:09:54 2022

@author: victo
"""

import pandas as pd
adultos = pd.read_csv('adultos.csv')
ninos = pd.read_csv('ninoss.csv')

poba=adultos.iat[0,3]
pobn=ninos.iat[0,3]
crin=ninos.iat[9,1]
print(f"De acuerdo al censo del 2021 de Canada, hay {poba} adultos desde los 18 hasta los 100 años \n")

choice=input('¿Le gustaria saber cuantas personas son detenidas al año? s/n \n') 
if choice == 's':
    print(f'{adultos.iat[7,1]} adultos son detenidos al año.')
else:
    print('\n ¿¡Qué, como que no?! \n \n')

print(f" \n\n En el caso de los niños, hay {pobn} menores residiendo en Canada, de los cuales {crin} han estado en correcionales. \n \n Ahora le mostraremos el menú de opciones: \n \n")

menu=0
while menu <=6:
    print(' 1 Si quiere ver la taza de crimen de los adultos \n 2 Si quiere ver la taza de crimen de los niños \n 3 Si quiere comparar ambas tazas de crimen \n 4 Si quiere ver las razones por las que detienen a los adultos \n 5 Las razones por las que detienen a los niños \n 6 Para salir del programa')
    menu=int(input('Escoja una opción del menú. \n '))
    if  menu==1:
        print(f"La taza de crimen para la población adulta es de: {adultos.iat[3,3]} % \n")
    elif menu== 2:
        print(f"La taza de crimen para la población de menores es de: {ninos.iat[4,3]} % \n")
    elif menu == 3:
        print(f'La taza de crimen de los niños es {adultos.iat[0,4]} puntos menor a la de los adultos \n')
    elif menu==4:
        print(pd.read_csv('adultos.csv', usecols=['TIPOS DE CONDENA','CANTIDAD']))
    elif menu==5 :
        print(pd.read_csv('ninoss.csv', usecols=['TIPOS DE CONDENA','CANTIDAD']))
    elif menu == 6:
        print('\n Gracias')
        break
        


# menu=int(input('Presione... \n 1 si quiere ver la taza de crimen de los adultos \n 2 si quiere ver la taza de crimen de los niños \n 3 si quiere comparar ambas tazas de crimen \n 4 si quiere ver las razones por las que detienen a los adultos \n 5 las razones por las que detienen a los niños \n 6 para salir del programa'))






# if menu <= 6:
#     while menu >= 0:
#         if menu == 1:
#             print(f"La taza de crimen para la población adulta es de {adultos.iat[3,3]}")
#             continue
#             print(menu)
#         elif menu == 2:
#             print(f"La taza de crimen para la población de menores es de {ninos.iat[3,3]}")
#             continue
#             print(menu)
#         elif menu == 6:
#             break








# print(ninos)

#poradul=pd.read_csv('adultos.csv', index_col=('POBLACION ADULTA'))

# porcen=adultos.iat[3,3]
# print(porcen)
