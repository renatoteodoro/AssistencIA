# Setup — Ambiente de Desenvolvimento

## Pré-requisitos

- Python 3.12+
- Git

## Instalação

```bash
# Clone o repositório
git clone <url-do-repositorio>
cd AssistencIA

# Crie e ative o ambiente virtual
python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # Linux/macOS

# Instale as dependências
pip install -r requirements.txt

# Aplique as migrations
python manage.py migrate

# Inicie o servidor de desenvolvimento
python manage.py runserver
```

O projeto estará disponível em `http://127.0.0.1:8000`.

## Criar superusuário

```bash
python manage.py createsuperuser
```

## Dependências atuais

| Pacote | Versão |
|---|---|
| Django | 5.2.14 |
| asgiref | 3.11.1 |
| sqlparse | 0.5.5 |
| tzdata | 2026.2 |

## Observações

- O banco de dados é SQLite (`db.sqlite3`) — sem configuração externa necessária.
- O arquivo `db.sqlite3` não deve ser commitado.
- O diretório `.venv/` não deve ser commitado.
