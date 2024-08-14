while True:
    numero1 = float(input("digite o primeiro numero:\n"))
    numero2 = float(input("digite o segundo numero:\n"))
    print(numero1+numero2)
    pergunta = input("Quer continuar?\nS -> sim ; N -> não\n").upper()
    if pergunta == "S":
        continue
    elif pergunta == "N":
        break
    else:
        print("resposta invalida!\n")

