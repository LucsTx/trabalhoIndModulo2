
#Projeto Individual - Módulo II - Lucas Teixeira do Nascimento (FUNÇÕES)
 
''' Função que registra o candidato. A função recebe as variáveis 'e','t','p' e 's', que são inputs do usuário recebendo notas em relação aos testes. O retorno é uma string que agrupa as informações que o usuário inputou no formato eX_tX_pX_sX'''

def registrarCandidato ():
    e = input('Digite a nota da entrevista: ')
    t = input('Digite a nota do teste teórico: ')
    p = input('Digite a nota do teste prático: ')
    s = input ('Digite a nota da avaliação de softskills: ')
    return f"e{e}_t{t}_p{p}_s{s}"

''' A função buscaCandidato recebe os parâmetros que virão a ser listas quando a função for chamada. Dentro da função é criada uma lista vazia  que receberá os candidatos compatíveis com as condições informadas; para isso o laço de repetição percorre os candidados da lista "resultados". '''


def buscaCandidato (resultados,notaMin):
    candidatosDispo = []
    for i,resultado in enumerate(resultados):
        notas = resultado.split('_')
        e,t,p,s = notas[0][1:], notas[1][1:], notas[2][1:], notas[3][1:]
        if int(e) >= notaMin[0] and int(t) >= notaMin[1] and int(p) >= notaMin [2] and int (s) >= notaMin[3]:
            candPosicao = f'Candidato {i+1}'
            candidatosDispo.append((candPosicao,resultado))
    return candidatosDispo 

