# TaskTracker

Aplicação de linha de comando (CLI) em Python para organizar tarefas.
Projeto do **Bootcamp II** — Análise e Desenvolvimento de Sistemas (CEUB).

**Autor:** Vinicius F. Dalamura

## Descrição funcional

O TaskTracker permite cadastrar tarefas e visualizá-las em um menu contínuo:

1. Cadastrar nova tarefa
2. Visualizar tarefas cadastradas
3. Sair da aplicação

Cada tarefa possui: título, descrição, prioridade, data limite e status.

### Regras de negócio

- O **título** é obrigatório (vazio ou só espaços é rejeitado e o prompt se repete).
- A **prioridade** aceita apenas `Alta`, `Média` (ou `Media`) e `Baixa`.
- Toda tarefa nova começa com status **Pendente**.
- Se não houver tarefas, o sistema informa que não há registros.

## Tecnologias

- Python 3
- Git e GitHub

## Estrutura do projeto

```
tasktracker-projeto/
├── README.md
├── .gitignore
├── docs/
│   └── planejamento_logico.pdf
└── src/
    └── main.py
```

## Instalação e execução

```bash
git clone https://github.com/ViniDalamura/tasktracker-projeto.git
cd tasktracker-projeto
python src/main.py
```

É necessário ter o Python 3 instalado. Não há dependências externas.

## Roadmap

- Fase 3: empacotamento, Docker, testes e deploy.
