from calculator import Calculator

calc = Calculator(filename="numbers.txt")

medias = calc.avg_file()

print(medias)

numeros = calc._ensure_casted_data()

somas = [sum(linha) for linha in numeros]

print(somas)