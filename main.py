import re

def carregarVocabulario(filename):
  dic = set()
  for line in open(filename, 'r', encoding='utf8'):
    dic.add(line.rstrip().lower())
  return sorted(dic)

dic = carregarVocabulario('vocabulario.txt')

def gerarPalavras(texto):
    lista = re.split('[0-9\s\W]',texto)
    result_list = list()
    for p in lista:
        if p != '':
            result_list.append(p)
    return result_list
    
def mmLetras(palavra1, palavra2):
    tamanho1 = len(palavra1)
    tamanho2 = len(palavra2)
    lista1 = list()
    lista2 = list()
    maior = 0
    for l in palavra1:
        lista1.append(l)
    for l in palavra2:
        lista2.append(l)
    if tamanho1 >= tamanho2:
        maior = tamanho1
        for i in range(tamanho2):
            if lista1[i] == lista2[i]:
                maior -= 1
    else:
        maior = tamanho2
        for i in range(tamanho1):
            if lista1[i] == lista2[i]:
                maior -= 1
    return maior

def lev(l,c,matriz):
    conta = matriz[l][c]
    return conta

def edicoes(palavra1, palavra2):

    if len(palavra1) == 0:
        return len(palavra2)
    elif len(palavra2) == 0:
        return len(palavra1)

    character1 = list()
    character2 = list()
    for letra in palavra1:
        character1.append(letra)
    for letra in palavra2:
        character2.append(letra)

    tamanho1 = len(palavra1)+1
    tamanho2 = len(palavra2)+1
    matriz = list()
    
    for l in range(tamanho1):
        lista = list()
        for c in range(tamanho2):
            lista.append(0)
        matriz.append(lista)

    for linha in range(tamanho1):
        for coluna in range(tamanho2):
            if linha == 0:
                matriz[0][coluna] = coluna
            elif coluna == 0:
                matriz[linha][0] = linha

    for l in range(1,tamanho1):
        for c in range(1,tamanho2):
            L = lev(l-1,c,matriz)+1
            E = lev(l,c-1,matriz)+1
            if character1[l-1] != character2[c-1]:
                V = lev(l-1,c-1,matriz)+1
            else:
                V = lev(l-1,c-1,matriz)+0
            matriz[l][c] = min(L,E,V)
    
    for l in range(tamanho1):
        for c in range(tamanho2):
            if l == tamanho1-1 and c == tamanho2-1:

                return matriz[l][c]
    
def sugerir(dic, palavra, distancia, maxSugestoes=5):

  initList = list()

  resultList = list()

  for i in range(len(dic)):

    initList.append(distancia(palavra,dic[i]))

  minDistancia = min(initList)

  count = 0

  while len(resultList) < maxSugestoes:
    for i in range(len(initList)):
      if minDistancia - 1 < initList[i] <= minDistancia:
        resultList.append(dic[i])
        if len(resultList) == maxSugestoes:
          break
        
    minDistancia +=1
    
  finalList = sorted(resultList)

  return finalList[:maxSugestoes]


def corretor(dic, texto, distancia, maxSugestoes=5):

  initList = gerarPalavras(texto)
  resultList = list()
  
  for i in range(len(initList)):
    if initList[i] not in dic:
      resultList.append(initList[i])

  finalList = list()
  for i in range(len(resultList)):
    finalList.append(sugerir(dic,resultList[i],distancia,maxSugestoes))
    
  for i in range(len(finalList)):

    print(resultList[i], '-->' , finalList[i])
      

  
        








