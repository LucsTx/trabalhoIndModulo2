
#Projeto Individual - Módulo II - Lucas Teixeira do Nascimento (FUNÇÕES)
 
''' Criando uma função que registra o candidato. A função recebe as variáveis 'e','t','p' e 's', que são inputs do usuário recebendo notas em relação aos testes. O retorno é uma string que agrupa as informações que o usuário inputou no formato eX_tX_pX_sX'''



def registrarCandidato ():
    e = input('Digite a nota da entrevista: ')
    t = input('Digite a nota do teste teórico: ')
    p = input('Digite a nota do teste prático: ')
    s = input ('Digite a nota da avaliação de softskills: ')
    return f"e{e}_t{t}_p{p}_s{s}"

''' A função buscaCandidato recebe os parâmetros 'resultados' e 'notaMin', que virão a ser listas quando a função for chamada. Dentro da função é criada uma lista vazia 'candidatosDispo', que receberá os candidatos compatíveis com as condições informadas. Dentro do laço for, o resultado do candidato cadastrado recebe a função 'split' que irá dividir a string que o usuário inputou, e atribui as partes divididas as variáveis 'e','t','p' e 's'. Para fazer atribuição primeiro foi criado uma variável "notas" que percorreu a lista 'resultados' declarada no arquivo main. Então pra cada resultado, até então em forma de string, a função split separa o resultado em sub elementos, cortando o "_". Após isso precisavamos converter essas strings em inteiros, para poder fazer a comparação com os inputs do usuário. Então em cada indice de "notas" a indexação "[1:]" fatia a string, retirando a letra "e","t" "p" e "s" da string, assim ficando só os numeros, agora num formato inteiro. E na sequencia dos índices a atribuição era feita as variáveis 'e', 't', 'p' e 's'. A condicionante if comparou os valores das variáveis com o valor dos indices da lista 'notaMin', declarada no arquivo main. Caso as condicionantes fossem verdadeiras, a lista candidatosDispo, recebia o candidato com o resultado compativel. A variável 'candPosição' recebia o valor de uma string com 'i+1', para que fosse adicionado a lista não só a nota, mas a identificação do candidato. Vale ressaltar também, que para indexar dois tipos de elementos dentro de 'resultados', foi utilizado o método "enumerate" que permitiu percorrer o índice dos candidatos, e também suas respectivas notas. '''


def buscaCandidato (resultados,notaMin):
    candidatosDispo = []
    for i,resultado in enumerate(resultados):
        notas = resultado.split('_')
        e,t,p,s = notas[0][1:], notas[1][1:], notas[2][1:], notas[3][1:]
        if int(e) >= notaMin[0] and int(t) >= notaMin[1] and int(p) >= notaMin [2] and int (s) >= notaMin[3]:
            candPosicao = f'Candidato {i+1}'
            candidatosDispo.append((candPosicao,resultado))
    return candidatosDispo 

