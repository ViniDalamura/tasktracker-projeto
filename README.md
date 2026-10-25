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
- Docker e Docker Compose

## Estrutura do projeto

    tasktracker-projeto/
    ├── .gitignore
    ├── .dockerignore
    ├── docs/
    │   └── planejamento_logico.pdf
    ├── src/
    │   └── main.py
    ├── Dockerfile
    ├── docker-compose.yml
    └── README.md

## Execução local (sem Docker)

    git clone https://github.com/ViniDalamura/tasktracker-projeto.git
    cd tasktracker-projeto
    python src/main.py

## Guia Docker

Pré-requisito: Docker Desktop instalado e em execução.

Como construir a imagem:

    docker build -t tasktracker-app .

Como rodar o container em modo isolado:

    docker run -it --rm tasktracker-app

Como rodar via orquestração (recomendado):

    docker compose run --rm tasktracker-app

### Decisões técnicas

- `FROM python:3.11-slim`: imagem oficial do Python em versão enxuta, com tamanho reduzido.
- `WORKDIR /app`: define a pasta de trabalho dentro do container.
- `ENV PYTHONUNBUFFERED=1`: envia a saída do programa ao terminal imediatamente, sem buffer.
- `COPY src/ /app/src/`: copia o código-fonte para dentro da imagem.
- `CMD ["python", "src/main.py"]`: comando que inicia a aplicação ao subir o container.
- `stdin_open: true` e `tty: true` no `docker-compose.yml`: mantêm a entrada do teclado aberta e alocam um terminal virtual, necessários porque o programa usa `input()`.
