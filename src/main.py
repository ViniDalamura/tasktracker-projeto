def exibir_menu():
    print("\n=== TASKTRACKER ===")
    print("1. Cadastrar nova tarefa")
    print("2. Visualizar tarefas cadastradas")
    print("3. Sair da aplicação")


def cadastrar_tarefa(tarefas):
    print("\n--- Cadastrar nova tarefa ---")
    titulo = input("Título: ")
    descricao = input("Descrição: ")
    prioridade = input("Prioridade: ")
    data_limite = input("Data limite (ex: DD/MM/AAAA): ")

    tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": "Pendente",
    }
    tarefas.append(tarefa)
    print("Tarefa cadastrada com sucesso!")


def visualizar_tarefas(tarefas):
    print("\n--- Tarefas cadastradas ---")
    if not tarefas:
        print("Não há tarefas cadastradas no momento.")
        return

    for numero, tarefa in enumerate(tarefas, start=1):
        print(f"\nTarefa {numero}")
        print(f"  Título.......: {tarefa['titulo']}")
        print(f"  Descrição....: {tarefa['descricao']}")
        print(f"  Prioridade...: {tarefa['prioridade']}")
        print(f"  Data limite..: {tarefa['data_limite']}")
        print(f"  Status.......: {tarefa['status']}")


def main():
    tarefas = []
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_tarefa(tarefas)
        elif opcao == "2":
            visualizar_tarefas(tarefas)
        elif opcao == "3":
            print("Encerrando o TaskTracker. Até logo!")
            break
        else:
            print("Opção inválida. Escolha 1, 2 ou 3.")


if __name__ == "__main__":
    main()
