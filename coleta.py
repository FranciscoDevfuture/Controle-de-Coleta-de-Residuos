import datetime

# Dicionário principal
dados_da_coleta = {}

# Função para coletar dados
def coleta_dados():
    global dados_da_coleta  # <- importante

    terminal = input("Digite o terminal: ")
    placa = input("Digite a placa: ")
    coleta = input("Digite a coleta: ")
    prefixo = input("Digite o prefixo: ")
    motorista = input("Digite o nome do motorista: ")
    rg = input("Digite o RG: ")
    MRT = input("Digite o MRT: ")
    
    try:
        sacos_comuns = int(input("Digite a quantidade de sacos comuns: "))
        sacos_reciclaveis = int(input("Digite a quantidade de sacos recicláveis: "))
    except ValueError:
        print("Erro: Digite números válidos para os sacos.")
        return

    horario_chegada = input("Digite o horário de chegada: ")
    horario_saida = input("Digite o horário de saída: ")
    observacoes = input("Digite as observações: ")
    colaboradores = input("Digite os colaboradores (separados por vírgula): ").split(",")

    # Atualiza o dicionário global
    dados_da_coleta = {
        "data": datetime.date.today(),
        "Terminal": terminal,
        "placa": placa,
        "coleta": coleta,
        "prefixo": prefixo,
        "nome_motorista": motorista,
        "RG": rg,
        "MRT": MRT,
        "Sacos comuns": sacos_comuns,
        "Sacos recicláveis": sacos_reciclaveis,
        "horario chegada": horario_chegada,
        "horario saida": horario_saida,
        "observacoes": observacoes,
        "Colaboradores": [col.strip() for col in colaboradores]
    }

# Exibir dados
def exibir_dados():
    if not dados_da_coleta:
        print("Nenhum dado coletado ainda.")
        return

    print(f"data: {dados_da_coleta['data']}")
    print(f"Terminal: {dados_da_coleta['Terminal']}")
    print(f"placa: {dados_da_coleta['placa']}")
    print(f"coleta: {dados_da_coleta['coleta']}")
    print(f"prefixo: {dados_da_coleta['prefixo']}")
    print(f"nome_motorista: {dados_da_coleta['nome_motorista']}")
    print(f"RG: {dados_da_coleta['RG']}")
    print(f"MRT: {dados_da_coleta['MRT']}")
    print(f"Sacos comuns: {dados_da_coleta['Sacos comuns']}")
    print(f"Sacos recicláveis: {dados_da_coleta['Sacos recicláveis']}")
    print(f"horario chegada: {dados_da_coleta['horario chegada']}")
    print(f"horario saida: {dados_da_coleta['horario saida']}")
    print(f"observacoes: {dados_da_coleta['observacoes']}")
    print(f"Colaboradores: {', '.join(dados_da_coleta['Colaboradores'])}")

# Salvar dados
def salvar_dados():
    try:
        with open("dados_coleta.txt", "a") as arquivo:
            arquivo.write("\n--- NOVA COLETA ---\n")
            arquivo.write(f"data: {dados_da_coleta['data']}\n")
            arquivo.write(f"Terminal: {dados_da_coleta['Terminal']}\n")
            arquivo.write(f"placa: {dados_da_coleta['placa']}\n")
            arquivo.write(f"coleta: {dados_da_coleta['coleta']}\n")
            arquivo.write(f"prefixo: {dados_da_coleta['prefixo']}\n")
            arquivo.write(f"nome_motorista: {dados_da_coleta['nome_motorista']}\n")
            arquivo.write(f"RG: {dados_da_coleta['RG']}\n")
            arquivo.write(f"MRT: {dados_da_coleta['MRT']}\n")
            arquivo.write(f"Sacos comuns: {dados_da_coleta['Sacos comuns']}\n")
            arquivo.write(f"Sacos recicláveis: {dados_da_coleta['Sacos recicláveis']}\n")
            arquivo.write(f"horario chegada: {dados_da_coleta['horario chegada']}\n")
            arquivo.write(f"horario saida: {dados_da_coleta['horario saida']}\n")
            arquivo.write(f"observacoes: {dados_da_coleta['observacoes']}\n")
            arquivo.write(f"Colaboradores: {', '.join(dados_da_coleta['Colaboradores'])}\n")
        print("Dados salvos com sucesso!")
    except Exception as e:
        print(f"Erro ao salvar dados: {e}")

# Carregar dados do arquivo
def carregar_dados():
    try:
        with open("dados_coleta.txt", "r") as arquivo:
            conteudo = arquivo.read()
            print("\nConteúdo do arquivo:\n")
            print(conteudo)
    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except Exception as e:
        print(f"Erro ao carregar dados: {e}")

# Menu principal
def main():
    while True:
        print("\nSistema de Controle de Coleta de Lixo")
        print("1. Coletar dados da coleta")
        print("2. Exibir dados da coleta atual")
        print("3. Salvar dados da coleta")
        print("4. Carregar dados do arquivo")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            coleta_dados()
        elif opcao == "2":
            exibir_dados()
        elif opcao == "3":
            salvar_dados()
        elif opcao == "4":
            carregar_dados()
        elif opcao == "5":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
