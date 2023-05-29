print("   ___       __         ________   __ \n  / _ |__ __/ /____    / __/ __ \ / / \n / __ / // / __/ _ \  _\ \/ /_/ // /__\n/_/ |_\_,_/\__/\___/ /___/\___\_/____/\n                                      ")
print("==========Bem vindo ao Auto SQL!==========\nInsira a quantidade de tabelas:")
qnt_tables = int(input())
tables = []
i = 0
while i < qnt_tables:
    tables.append(i)
    i += 1

for i in tables:
    print("Insira o Título da table", tables[i], ":")
    tables[i] = input()

for i in tables:
    print("Insira o Título da table", tables[i], ":")
    tables[i] = input()
print(tables)