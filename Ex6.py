#Leia o nome de N pessoas e informe o nome da pessoa mais velha que tenha idade par.
idade1=0
nomex = str()
while True:
    idade = int(input("Informe a sua idade"))
    nome=str(input("Informe o seu nome"))
    if idade > idade1:
        if idade % 2 == 0:
            nomex = nome
    stop = int(input("Se quiser encerrar a entrada de dados digite 1, se quiser continuar digite 2"))
    if stop == 1:
        break
print("A pessoa mais velha com idade par é",nomex)