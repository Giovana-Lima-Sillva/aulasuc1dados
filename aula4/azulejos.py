import math

comprimento = float(input("Digite o comprimento da cozinha (m): "))
largura = float(input("Digite a largura da cozinha (m): "))
altura = float(input("Digite a altura da cozinha (m): "))

if comprimento <= 0 or largura <= 0 or altura <= 0:
    print("Erro: As dimensões devem ser maiores que zero.")
else:
    # Calcular a área da cozinha
    area = 2 * (comprimento + largura) * altura
    caixas = math.ceil(area / 1.5)  # Cada caixa cobre 1,5 m²
    print(f"A área da cozinha é: {area:.2f} m²")
    print(f"Quantidade de caixas necessárias: {caixas}")