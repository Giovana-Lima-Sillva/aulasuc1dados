nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
optativa = float(input("Digite a nota da optativa (-1 se não fez): "))

if optativa != -1:
    if nota1 < nota2 and optativa > nota1:
        nota1 = optativa
    elif nota2 <= nota1 and optativa > nota2:
        nota2 = optativa

media = (nota1 + nota2) / 2

if media >= 6:
    situacao = "Aprovado"
elif media >= 3:
    situacao = "Exame"
else:
    situacao = "Reprovado"

print(f"Média: {media:.1f} - {situacao}")