from time import sleep

class Arq:
    def __init__ (self, nomearq):
        try:
            self.arquivo = open(nomearq,"r")       # r = leitura dos arquivos       open = abrir o arquivo
            self.lista_Arq = (self.arquivo.readlines()) #Lê do arquivo para uma lista
        except Exception as error:
            print(error)
            exit()
    
    #SUCESSORES DO VALOR INFORMADO PELO USUÁRIO    
    def sucessores(self,User):
        print("_____________________________________________________")
        print("Os sucessores são:")
        cont = 0                    #Conta graus
        sup = 0                      #variavel de suporte
        for i in self.lista_Arq:
            aux = 0
            listsplit=(i.split("   "))        #Split dos espasos vazios
            listfilter = list(filter(("").__ne__, listsplit))
            if sup == 1:
                while aux == 0:
                    if listfilter[aux] == " "+str(User):
                        print(listfilter[1].strip("\n").strip(" "))  #printa as respostas
                        cont += 1
                    elif listfilter[aux] ==  "  "+str(User):
                        print(listfilter[1].strip("\n").strip(" "))  #printa as respostas
                        cont += 1
                    elif listfilter[aux] == str(User):
                        print(listfilter[1].strip("\n").strip(" "))  #printa as respostas
                        cont += 1
                    aux += 1
            sup=1
        print("_____________________________________________________")
        return cont            #retorna o contador do grau

    def predecessores(self,User):
        print("_____________________________________________________")
        print("Os predecessores são:")
        cont = 0        #Conta grau
        sup=0
        for i in self.lista_Arq:
            aux = 1
            listsplit=(i.split("   "))        #Split dos espasos vazios
            listfilter = list(filter(("").__ne__, listsplit))
            if sup == 1:
                while aux == 1:
                    if listfilter[aux] == " "+str(User)+"\n":
                        print(listfilter[0].strip("\n").strip(" "))  #printa as respostas
                        cont += 1
                    elif listfilter[aux] ==  "  "+str(User)+"\n":
                        print(listfilter[0].strip("\n").strip(" "))  #printa as respostas
                        cont += 1
                    elif listfilter[aux] == str(User)+"\n":
                        print(listfilter[0].strip("\n").strip(" "))  #printa as respostas
                        cont += 1
                    aux += 1
            sup=1
        print("_____________________________________________________")
        return cont                 #retorna o contador do grau