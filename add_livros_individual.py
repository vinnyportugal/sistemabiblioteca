import mysql.connector

def add_livro_individual():

    try:

        conexao = mysql.connector.connect(
            user = '******',
            password = '******',
            database = '********'
        )

        cursor = conexao.cursor

        add_livro = ''' INSERT INTO livraria ( id_livro_biblioteca , nome , paginas , compra) VALUES (%s , %s , %s , %s) '''
        dados = ( 0 , ' ', '' , '' )

        cursor = conexao.cursor()
        cursor.execute(add_livro , dados)
        conexao.commit()

        while True:
            for linha in add_livro:
                print(linha)
                break
            print(' livro cadastrado com sucesso!!')
            break


        cursor.close()
        conexao.close()




    except mysql.connector.errors.ProgrammingError:
        print(' algo deu errado, tente novamente!!')









add_livro_individual()


