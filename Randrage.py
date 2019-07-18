import statistics as s
import random as r 

v_lista = []
i = 2

while i<=20:
  v_lista.append(r.randrange(1,100,3))
  i+=1

print(f'Essa foi a lista gerada aleatóriamente: {v_lista}')

def maior(v_lista):
  return max(v_lista, key=int)

print(f'O maior valor desta lista é: {maior(v_lista)}')
 
print(f'sua média é :{mean(v_lista)}')