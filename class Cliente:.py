class Cliente:
    def __init__(self, nome, rg, endereco, telefone, placacarro, modelo, ano):
        self.nome = nome
        self.rg = rg
        self.endereco = endereco
        self.telefone = telefone
        self.placacarro = placacarro
        self.modelo = modelo
        self.ano = ano

class Borracharia:
    def manutencao_geral(self, cliente):
        print(f"A manutenção geral do veículo do cliente {cliente.nome} foi realizada com sucesso.")
    
    def organizar_clientes(self, lista_clientes):
        return sorted(lista_clientes, key=lambda cliente: cliente.nome)

class Funcionario:
    def __init__(self, salario, informacoes_pessoais):
        self.salario = salario
        self.informacoes_pessoais = informacoes_pessoais

def obter_dados_cliente():
    nome = input("Digite o nome do cliente: ")
    rg = input("Digite o RG do cliente: ")
    endereco = input("Digite o endereço do cliente: ")
    telefone = input("Digite o telefone do cliente: ")
    placacarro = input("Digite a placa do carro do cliente: ")
    modelo = input("Digite o modelo do carro do cliente: ")
    ano = input("Digite o ano do carro do cliente: ")

    return Cliente(nome, rg, endereco, telefone, placacarro, modelo, ano)

def obter_status_pedido():
    status = input("Digite o status do pedido: ")
    return status

def main():
    lista_clientes = []
    borracharia = Borracharia()

    while True:
        opcao = input("Digite 1 para cadastrar um novo cliente, 2 para realizar a manutenção geral ou 3 para sair: ")

        if opcao == "1":
            cliente = obter_dados_cliente()
            lista_clientes.append(cliente)
        elif opcao == "2":
            if len(lista_clientes) == 0:
                print("Não há clientes cadastrados.")
                continue

            borracharia_organizada = borracharia.organizar_clientes(lista_clientes)
            
            print("Clientes cadastrados:")
            for cliente in borracharia_organizada:
                print(f"Nome: {cliente.nome}")
                print(f"RG: {cliente.rg}")
                print(f"Endereço: {cliente.endereco}")
                print(f"Telefone: {cliente.telefone}")
                print(f"Placa do Carro: {cliente.placacarro}")
                print(f"Modelo do Carro: {cliente.modelo}")
                print(f"Ano do Carro: {cliente.ano}")
                print()
        elif opcao == "3":
            break

if __name__ == "__main__":
    main()
