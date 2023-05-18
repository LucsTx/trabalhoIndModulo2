
#Projeto Individual - Módulo II - Lucas Teixeira do Nascimento (MAIN)
''' Essa é a tela principal que fará modulação de todas as funções do arquivo 'funçõesTrabalhoInd' por meio do método "import *". '''

from funcoesTrabalhoInd import *

resultados = []
numeroCand = int(input('Quantos candidatos deseja cadastrar?'))

''' Percorrendo o numero de candidatos presente na variável numeroCand. E adicionando os candidatos à lista "resultados". '''

for i in range(numeroCand):
    print(f'\nCandidato {i+1}')
    resultado = registrarCandidato ()
    resultados.append (resultado)

''' A lista 'notaMin' inicia-se vazia, para depois a cada input do usuário, que digitará a nota minima exigita, componha a lista na ultima posição. Essas posições serão usadas na função "buscaCandidato" dentro da condicionante 'if'. '''


notaMin = []
notaMin.append(int(input('\n Digite a nota de corte para entrevista: ')))
notaMin.append(int(input('Digita a nota de corte para o teste teórico: ')))
notaMin.append(int(input('Digite a nota de corte para o teste prático: ')))
notaMin.append(int(input('Digite a nota de corte para a avaliação de softskills: ')))

''' A variável candidatos chaama a função buscaCandidato com os parâmetros que já estão declarados aqui no Main. '''

candidatos = buscaCandidato (resultados,notaMin)

print ('\nCandidatos compatíveis: \n')

''' Print dos candidatos compatíveis.'''

for candidato in candidatos:
    print(candidato) 


