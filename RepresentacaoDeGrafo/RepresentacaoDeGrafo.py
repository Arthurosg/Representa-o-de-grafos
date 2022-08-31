from datetime import datetime           
from arquivo import Arq                                                                       #imports (arquivo)
from time import sleep

nomearq = input("Qual o nome do arquivo texto?\n|EX: graph-test-100.txt|\n= ")
print("_____________________________________________________")
User = input("Qual numero do vertice?\n= ")
arq = Arq(nomearq)

print("O grau de saida é: ",arq.sucessores(User))
print("O grau de entrada é: ",arq.predecessores(User))



        