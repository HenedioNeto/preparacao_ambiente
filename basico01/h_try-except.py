#Erros, exceções e tratamentos de erro
#Quando o erro não se da de forma sintatica ele é chamado de exceção
"""
n = int(input('num')) no caso acima não há erro sintatico e recebendo um valor de inteiro no input 
ira rodar tranquilamente, porém, por pedir um inteiro, caso a pessoa coloque uma string ou um
float ele tera uma exceção
"""
#Existem diversos tipos de erros(exceções), erro de valor, erro de input etc...
#Ao tratarmos esses erros conseguimos informar de forma mais legivel qual erro no terminal
"""
Outro exemplo de exceção é:
Pedimos no input dois numero, a e b, o a será dividido por b
Nesse caso não há problema caso seja informado 5 e 2 (a resposta sera 2,5)
Porém há exceções, caso o dado fornecido para o b seja 0 (não há divisões por 0), outro exemplo é
caso o b seja '1' ou 'um', nesse caso seria um TypeError onde o dado fornecido é uma string e não
há como dividir numero por string
Exceções com lista: dado a lista = [1, 2, 3]
O print(lista[3]) será uma exceção por n possuir tal indice na lista/ no caso da lista sera IndexError
caso seja um dicionario sera KeyError
Há exceções para import de modulos que não existe
etc...
"""

#Ao comunicarmos com uma linguagem tratando erros, damos o comando de try(para que o programa tente algo)
"""
try:
    a = int(input('Num1'))
    b = int(input('Num2'))
    r = a / b
except:
    print('Ocorreu um erro com a divisão')
else: #bloco de codigo para caso não de problema
    print(r)
finally: #vai acontecer independente se der erro ou não
    print('Fim do programa, espero que tenha dado certo')
    break
"""

#o try pode ter varios except, cada um com seu proprio tipo de erro e tratamento

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO: digite um numero inteiro ou válido.')
            continue
        except (keyBoardInterrupt):
            print('Entrada de dados interrompida pelo usuário.')
            break
        else:
            return n

num = leiaInt('Digite um valor:\n')
print(f'O valor digitado foi {num}')