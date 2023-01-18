<p align="center">
  <a href="https://github.com/zev4l/chessbook">
    <img src="https://www.palpitedigital.com/y/322/corretor-e1444142590776.jpg" alt="Logo" width="80" height="80">
  </a>

<h1 align="center">Corretor Ortográfico</h3>
<h4 align="center">Projeto para a cadeira de Programação 1 (2020/2021)</h5>

## Objetivo
O objetivo deste projeto é criar um corretor ortográfico baseado num vocabulário disponível com um conjunto de palavras, o corretor lê uma string com texto e indicar todas as palavras que não reconhece. Para além disso, deve sugere correções baseadas num algoritmo de semelhança de palavras.

## Instruções 

### Função gerarPalavras 
Recebe uma string com texto, e devolve uma lista com as várias palavras contidas na string, pela ordem que aparecem.

```bash
python3 -c 'from main import *; print(gerarPalavras("YOUR TEXT HERE"))'
```

### Função mmLetras
Devolve a subtração entre o tamanho da maior palavra dada e o número de letras iguais nas mesmas posições entre as duas palavras

```bash
python3 -c 'from main import *; print(mmLetras("YOUR TEXT HERE", "YOUR TEXT HERE"))'
```

### Função edicoes 
Devolve o número mínimo de operações de edição necessárias para transformar uma palavra na outra 
As operações de edição podem ser as seguintes:
*inserir uma letra numa qualquer posição 
*apagar uma letra
*substituir uma letra por outra letra



