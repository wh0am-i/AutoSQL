print("   ___       __         ________   __ \n  / _ |__ __/ /____    / __/ __ \ / / \n / __ / // / __/ _ \  _\ \/ /_/ // /__\n/_/ |_\_,_/\__/\___/ /___/\___\_/____/\n                                      ")
print("==========Bem vindo ao Auto SQL!==========\nInsira a quantidade de tabelas:")
qnt_tables = int(input())
tables = []
colunas = []
atributos = []

i = 0
while i < qnt_tables:
    print("Insira o Título da table", i + 1, ":")
    tables.append(input())
    print("Insira a quantidade de colunas da tabela", tables[i], ":")
    colunas = int(input())
    x = 0
    while x < colunas:
        print("Insira o Título da coluna", x + 1, ":")
        colunas.append(input())
        print("Insira o tipo de atributo da coluna e se é not null", coluna[x], ":")
        atributos.append(input())
        x += 1
    i += 1