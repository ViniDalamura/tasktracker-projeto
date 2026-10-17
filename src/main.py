
PRIORIDADES_VALIDAS = {
    "alta": "Alta",
    "media": "Média",
    "média": "Média",
    "baixa": "Baixa",
}


def exibir_menu():
    print("\n=== TASKTRACKER ===")
    print("1. Cadastrar nova tarefa")
    print("2. Visualizar tarefas cadastradas")
    print("3. Concluir tarefa")
    print("4. Sair da aplicação")


def pedir_titulo():
    while True:
        titulo = input("Título: ").strip()
        if titulo:
            return titulo
        print("Erro: o título é obrigatório e não pode ficar vazio.")


def pedir_prioridade():
    while True:
        entrada = input("Prioridade (Alta, Média ou Baixa): ").strip().lower()
        if entrada in PRIORIDADES_VALIDAS:
            return PRIORIDADES_VALIDAS[entrada]
        print("Erro: prioridade inválida. Digite Alta, Média ou Baixa.")


def cadastrar_tarefa(tarefas):
    print("\n--- Cadastrar nova tarefa ---")
    titulo = pedir_titulo()
    descricao = input("Descrição: ").strip()
    prioridade = pedir_prioridade()
    data_limite = input("Data limite (ex: DD/MM/AAAA): ").strip()

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
        print(f"  Descrição....: {tarefa['descricao'] or '(sem descrição)'}")
        print(f"  Prioridade...: {tarefa['prioridade']}")
        print(f"  Data limite..: {tarefa['data_limite'] or '(não informada)'}")
        print(f"  Status.......: {tarefa['status']}")


def concluir_tarefa(tarefas):
    print("\n--- Concluir tarefa ---")

    if not tarefas:
        print("Não há tarefas cadastradas no momento.")
        return

    visualizar_tarefas(tarefas)

    try:
        numero = int(
            input("\nDigite o número da tarefa que deseja concluir: ")
        )

        if numero < 1 or numero > len(tarefas):
            print("Erro: número de tarefa inválido.")
            return

        tarefa = tarefas[numero - 1]

        if tarefa["status"] == "Concluída":
            print("Esta tarefa já foi concluída.")
        else:
            tarefa["status"] = "Concluída"
            print("Tarefa concluída com sucesso!")

    except ValueError:
        print("Erro: digite um número válido.")


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
            concluir_tarefa(tarefas)
        elif opcao == "4":
            print("Encerrando o TaskTracker. Até logo!")
            break
        else:
            print("Opção inválida. Escolha 1, 2, 3 ou 4.")


if __name__ == "__main__":
    main()
