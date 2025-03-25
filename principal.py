import mysql.connector
import sqlite3
import time
from time import sleep


t = 5
conexao = mysql.connector.connect(
    user = '*****',
    password = '******',
    database = '*******'
)
lista = []
cursor = conexao.cursor
#id = 0
id_livro_biblioteca = 0
acumulador = id_livro_biblioteca



def id_sistema():

    conexao = mysql.connector.connect(
        user='*****',
        password='********',
        database='*******'
    )

    cursor = conexao.cursor
    id_livro_biblioteca = 0
    acumulador = id_livro_biblioteca + 1
    biblioteca_id = {'id_livro_biblioteca' : id_livro_biblioteca }
    inserir = '''INSERT INTO livraria ( id_livro_biblioteca ) VALUES ( %s )'''
    dado = (id_livro_biblioteca)
    cursor = conexao.cursor()
    cursor.execute( dado)


    conexao.commit()
    print( 'ID DO LIVRO : >>> {}'.format(acumulador))

    conexao.close()
    cursor.close()
def blibioteca():
    conexao = mysql.connector.connect(
        user='*****',
        password='******',
        database='*****'
    )
    try:
        while True:

            cursor = conexao.cursor
            id_livro_biblioteca = ()
            #id_sistema()
            nome = input(' qual o livro deseja cadastrar? >>> ')
            paginas = int(input(' qual o numero de paginas? >>> '))
            compra = input(' lugar de compra do livro: >>> ')
            blibioteca_livro = { 'id_livro_biblioteca' : id_livro_biblioteca,                                                     # funcao de cadastro do nosso banco de dados!!
                                ' nome ': nome,
                                ' paginas': paginas,
                                'compra': compra}
            lista.append(blibioteca_livro.copy())


            inserir = '''INSERT INTO livraria (  nome , paginas , compra) VALUES ( %s ,%s , %s)'''

            dados = ( nome , paginas , compra)
            cursor = conexao.cursor()
            cursor.execute(inserir , dados)
            conexao.commit()                            # o commit serve para salvar todos os dados que inserimos em nossa tabela!!
            break

    except ValueError:
        print(' digite a funcao correta!!')
        return blibioteca()

    finally:
        conexao.close()

        while True:



            condicao = input(' voce deseja cadastrar outro livro? (S / N):'
                                 '>>> ')
            condicao = condicao.lower() and condicao.upper()

            while condicao == 'S' and 's':
                print(' vamos cadastrar mais livros entao!')
                return blibioteca()
            while condicao == 'N' and 'n':
                print(' SAINDO...')
                time.sleep(t)
                return






#blibioteca(id)

def consutar_livro():
    conexao = mysql.connector.connect(
        user='****',
        password='***',
        database='*********'
    )
    cursor=conexao.cursor()
    global global_livro
    print(' CONSULTA DA MINHA BLIBIOTECA!!!!')
    while True:
        funcao = input(' | QUAL A FUNCAO DESEJADA :              \n ' +
                       '| 1 - CONSULTAR TODOS OS LIVROS          \n   ' +
                     '  |  2 - CONSUTAR LIVRO PELO ID             \n ' +                       # funcao para consulta do nosso banco de dados!!
                       '| 3 - CONSULTAR PELO NOME                \n ' +
                       '| 4 - RETORNAR                         \n  ' +
                       '>>> ')
        if funcao == '1':
            print(' CONSULTAR TODOS OS LIVROS CADASTRADOS')
            print(' - +' *15)
            cursor.execute('  SELECT * FROM livraria ' )
            resultado = cursor.fetchall()
            for linha in resultado:                                     # esse if consulta todos os dados do nosso banco!!
                print(' - +' * 15)
                print(linha)
                print(' - +' * 15)

            contagem = input('quantidade de livros -> {}'.format(len(resultado)))
            print('-+'*15)

            if not resultado:              # essa linha retorna a mensagem quando nao ha nenhum dado em nossa tabela!!
                print(' NAO EXISTE LIVROS CADASTRADOS !!..')
                return
        elif funcao == '2':
            print(' CONSULTAR LIVROS PELO ID')
            id_desejado = int(input(' QUAL O ID DESEJADO : >>> '))              # esse elif pesquisa o livro pelo id do livro!!



            cursor.execute('SELECT * FROM livraria WHERE  id_livro_biblioteca = {}'.format(id_desejado))
            print(' - +' * 30)
            consulta = cursor.fetchall()                                # o cursor.fetchall serve para retornar todas as linhas salvas em nosso banco!!
            for linha in consulta:
                print(' - +' * 30)                                                           # usei o for para retornar o valor(id) que eu pesquisei do meu banco de dados!!
                print(  linha )
                print(' - +' * 30)

        elif funcao == '3':
            try:
                print( ' CONSULTAR LIVROS PELO NOME' )

                nome_desejado = input(' QUAL O NOME DO LIVRO DESEJADO \n' 
                             '>>> ')
                query = ("SELECT FROM * livraria WHERE=nome: {}".format(nome_desejado))                   # esse elif serve para consultar o livro pelo nome!!
                cursor.execute(query)
                                                                                              # usei um try tambem para apresentar um erro quando o nome ou alguma coisa estiver errada, a famosa tratamento de erros!!
                nome_desejado = (nome_desejado.lower() and
                               nome_desejado.upper()   and
                               nome_desejado.strip())

                consulta_nome = cursor.fetchall()

                for linha in consulta_nome:                                                    # usei um for para retornar o valor!!!
                    print(linha)
            except mysql.connector.errors.ProgrammingError:
                print(' O NOME PESQUISADO ESTA ERRADO, FAVOR CONSULTAR PELO ID PARA MELHOR COMPREENÇÃO!!')                  # esta e amensagem que retorna quando da algum problema!
                return

        elif funcao == '4':
            print('AGUARDE UM MOMENTO...')                                  # esse elif retorna para o menu principal!!
            time.sleep(t)
            return

        else:
            print(' FUNCAO ERRADA! TENTE OUTRA VEZ')                            # usei o else quando o usuario digitar a funcao errada, com isso aparecerar essa mensagem e retornar para o menu!!
            continue
def remover_livro():
    conexao = mysql.connector.connect(
        user='****',
        password='**',
        database='******'
    )
    cursor = conexao.cursor()
    print(' REMOVENDO ALGUM LIVRO DA MINHA COLECAO!')
    id_livro_remover = input(' QUAL ID DO LIVRO QUE DESEJA REMOVER? \n'                       # essa funcao serve para remover algum livro de nossa tabela co banco de dados!!
                               '>>> ' )



    linha = cursor.execute('''DELETE FROM livraria WHERE id_livro_biblioteca = {}'''.format(id_livro_remover))
    cursor.fetchall()
    conexao.commit()

    for linha in id_livro_remover:                            # usei um for para retornar o id que deseja remover!!
        print(linha)

    while True:
        try:
            print(' LIVRO REMOVIDO COM SUCESSO!!...')                   # estou usando um while  para retornar a mensagem de remocao com sucesso! quando acionado, que dizer que foi removido com sucesso o livro!!
            return


        except mysql.connector.Error as err:                                # o try para tratamento de erro, que vai retornar uma mensagem que o livro nao foi removido... quando acionado alguma coisa estarar errada em nosso codigo!!
            print(' LIVRO NAO REMOVINDO!...')
            break



    if not remover_livro():                                             # essa linha retorna a mensagem quando nao ha nenhum dado em nossa tabela para remover!!
        print(' NAO EXISTE LIVROS CADASTRADOS !!..')
        return funcao2


    cursor.close()                                          # usando o cursor.close para fechar!!
    conexao.close()                             # usando o conexao.close para fechar a nossa conexao, so podemos repetir uma operacao depois que fechamos a anterior!!


def remover_tabela():
        conn = mysql.connector.connect(
            user='*****',
            password='****',
            database='*****'
        )
        cursor = conn.cursor()

        linha = cursor.execute(''' DELETE FROM livraria ''')

        delete = cursor.fetchall()
        conn.commit()

        for linha in delete:                              # essa funcao e somente se eu querer remover todos os livros da minha tabela de uma vez so!!
            print(linha)
                                                                # portanto nao usaremos ela mais!!!
        while True:
            try:
                print(' tabela excluida com sucesso!!')
                break

            except mysql.connector.Error as err:
                print(' ERRO AO CONECTAR AO BANCO DE DADOS!!')
                return

        cursor.close()
        conn.close()

#remover_tabela()

while True:
    funcao2 = input(' | QUAL A FUNCAO DESEJADA: \n ' +
                    '| 1 - CADASTRO DE LIVROS \n' +                         # aqui esta nosso menu!!
                    ' | 2 - CONSULTA DE LIVROS \n' +
                    ' | 3 - REMOCAO DE LIVROS \n' +
                    ' | 4 - SAIR \n'  +
                    '>>> ')
    if funcao2 == '1':
        id_sistema()
        blibioteca()
        break
    elif funcao2 == '2':
        consutar_livro()
    elif funcao2 == '3':
        remover_livro()
    elif funcao2 == '4':
        print(' SAINDO!!')
        time.sleep(t)
        break
    else:
        print(' FUNCAO ERRADA!! TENTE NOVAMENTE!!')
        continue



