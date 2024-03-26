import random

def cadastrarVoo(voos, origem, destino):
    numeroVoo = numeroVooAl()
    voos[numeroVoo] = {'origem': origem, 'destino': destino}

def contarOrigemVoo(voos, origem):
    quantidade = sum(1 for voo in voos.values() if voo['origem'] == origem)
    return quantidade

def numeroVooAl():
    numeroVoo = 'V' + str(random.randint(1, 999)).zfill(3)
    return numeroVoo

def main():
    voos = {}
    cadastrarVoo(voos, 'Natal', 'Porto Alegre')
    cadastrarVoo(voos, 'Natal', 'São Paulo')
    cadastrarVoo(voos, 'Porto Alegre', 'Natal')
    cadastrarVoo(voos, 'Natal', 'Brasilia')
    cadastrarVoo(voos, 'Manaus', 'Natal')
    
    print("Lista de voos cadastrados:")
    for numeroVoo, vooInfo in voos.items():
        print(f"Numero do Voo: {numeroVoo}, Origem: {vooInfo['origem']}, Destino: {vooInfo['destino']}")
    
    origemNatal = contarOrigemVoo(voos, 'Natal')
    print(f"\nQuantidade de voos com origem em Natal: {origemNatal}")

if __name__ == "__main__":
    main()
