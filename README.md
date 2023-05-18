<h1 align "center">
# Projeto Individual Módulo 2 - VAMO AI 
</h1>
<h1>

#Sobre 

Este projeto visa permitir que o usuário consulte a compatibilidade de candidatos dentro de um processo seletivo. O sistema recebe o número de candidatos que serão cadastrados, as notas desses candidatos e as notas de corte em cada uma dessas etapas de avaliação. No fim o sistema elege os candidatos compatíveis com os critérios estabelecidos junto com suas respectivas notas. 

#Como funciona? 

O projeto foi desenvolvido em Python (.py) dentro da IDE Visual Studio Code  e utiliza dois arquivos dentro do programa. O arquivo principal (mainTrabalhoInd.py) executa o código que interage com o usuário no terminal, e utiliza o método de  modularização para interagir com as funções do programa no segundo arquivo (funcoesTrabalhoInd.py). Para utilizar o usuário deve baixar o repositório e executar os dois arquivos. 


#Utilização do código

Após abrir os arquivos dentro do editor de textos, o usuário deve executar o código. Inicialmente é pedido o número de candidatos que se deseja cadastrar. Após essa etapa, deve-se inserir as notas de cada usuário nas etapas do processo seletivo (E- Entrevista, T- Teste Teórico, P- Teste Prático e S- Avaliação de SoftSkills). Ao ser feito o registro de todas as notas, o sistema pede as notas de corte para cada etapa de avaliação e por fim, com todos os registros feitos e os critérios já determinados, é exibido na tela os candidatos que são compatíveis com as notas de corte. 

#Por dentro do código

Basicamente, duas funções comandam o código. Dentro delas foi utilizado o conceito de listas. O laço de repetição "for" opera juntamente com o desvio de condicional "if" dentro das funções, fazendo indexação das listas que o usuário inputa, e retornando após as devidas verificações o candidato para a nova lista de candidatos compátiveis. Essas funções são modularizadas no arquivo principal através do arquivo Main, onde também são declaradas as variáveis. Mais informações sobre a estrutura do programa estão comentadas dentro do código.