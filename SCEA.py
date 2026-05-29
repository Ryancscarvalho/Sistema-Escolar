negrito = "\033[1m"
sublinhado = "\033[4m"
limpa = "\033[0m"

print("==========================================================")
nome = input("Bem-vindo, aluno! Digite seu nome: ")

while True:
    print("==========================================================")
    print(f"{negrito}Informações escolares!{limpa}")
    print(f"Olá, {nome}! Abaixo você pode acessar suas informações escolares:")
    print("[1] Ver boletim.")
    print("[2] Frequência.")
    print("[3] Verificar aprovação.")

    opcao = int(input("O que você deseja verificar? "))
    if opcao == 1:
        print("==========================================================")
        print(f"{negrito}Boletim escolar!{limpa}")
        nota1 = float(input("Digite sua primeira nota: "))
        nota2 = float(input("Digite sua segunda nota: "))
        nota3 = float(input("Digite sua terceira nota: "))
        nota4 = float(input("Digite sua quarta nota: "))
        print("==========================================================")

        media = (nota1 + nota2 + nota3 + nota4) /4

        print(f"Sua média é: {sublinhado}{negrito}{media}{limpa}")
    if opcao == 2:
        print("==========================================================")
        falta = int(input("Digite quantas faltas você teve no ano: "))
        print(f"Dias letivos totais: {sublinhado}{negrito}200{limpa}")
        print(f"Você tem {sublinhado}{negrito}{falta}{limpa} faltas")
        falta1 = 200-falta
        qntft = (falta1/200)*100
        if qntft >75:
            print(f"Sua frequência é de: {sublinhado}{negrito}{qntft}%.{limpa} Tudo certo!")
        else:
            print(f"Sua frequência é de: {sublinhado}{negrito}{qntft}%.{limpa} Você faltou demais!")
    if opcao == 3:
        print("==========================================================")
        print(f"{negrito}Verificação de Aprovação:{limpa}")
        mediaf = float(input("Qual sua média? "))
        freq = int(input("Qual sua frequência? "))
        if mediaf >= 7 and freq >= 75:
            print("Parabéns, você foi aprovado!")
        else:
            print("Infelizmente, você foi reprovado.")