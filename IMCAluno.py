def calcularImc(peso, estatura):
    return peso / (estatura ** 2)

alunos = {}

n = int(input("Quantos alunos deseja cadastrar? "))

for i in range(n):
    nome = input(f"Informe o nome do aluno {i+1}: ")
    altura = float(input(f"Informe a altura do aluno {i+1}: "))
    peso = float(input(f"Informe o peso em kg do mesmo {i+1}: "))
    alunos[nome] = {"altura": altura, "peso": peso}

print("\nAlunos cadastrados:")
for nome in sorted(alunos.keys()):
    info = alunos[nome]
    imc = calcularImc(info["peso"], info["altura"])
    print(f"Nome: {nome} - IMC: {imc:.2f}")