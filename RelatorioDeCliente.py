clientes = {
    "Cliente 1": 23521,
    "Cliente 2": 87456,
    "Cliente 3": 2399,
    "Cliente 4": 4329,
    "Cliente 5": 3523
}

clientesOrdenadosDesc = dict(sorted(clientes.items(), key=lambda item: item[1], reverse=True))

print("Relatório de Clientes Potenciais:")
for cliente, valorCompras in clientesOrdenadosDesc.items():
    print(f"Cliente: {cliente} - Total de Compras: R${valorCompras}")
