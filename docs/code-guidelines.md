# Code Guidelines

## Idioma

- **Código:** inglês — nomes de variáveis, funções, classes, arquivos, comentários.
- **Interface do usuário:** português brasileiro — labels, mensagens, textos exibidos ao usuário.

## Estilo Python

- Seguir **PEP8** rigorosamente. Verificar com `flake8`.
- Usar **aspas simples** (`'`) em todo o código Python.
- Sem comentários redundantes — só comentar o que não é óbvio pelo nome.

## Views

- Usar **Class-Based Views (CBV)** preferencialmente.
- Toda view autenticada deve usar `LoginRequiredMixin`.
- Toda view que acessa um objeto específico deve verificar ownership — retornar 404 se o objeto não pertencer ao `request.user`.

## Models

- Toda model deve ter os campos de auditoria:

```python
created_at = models.DateTimeField(auto_now_add=True)
updated_at = models.DateTimeField(auto_now=True)
```

- Chaves estrangeiras para o usuário devem referenciar `settings.AUTH_USER_MODEL`.

## Signals

- Signals devem residir em `signals.py` dentro da app correspondente.
- Conectar via `ready()` em `apps.py`.

## Formulários

- Usar `ModelForm` sempre que o formulário representar uma model.
- Filtrar querysets de campos relacionais pelo usuário logado no `__init__` do form.

## Querysets

- Nunca retornar dados sem filtrar por `user=request.user` em views autenticadas.
- Usar `get_queryset()` nas CBVs para aplicar o filtro.

## Regras de negócio obrigatórias

- **Exclusão de conta bloqueada** se houver transações vinculadas — verificar antes de deletar e exibir mensagem informativa.
- **Exclusão de categoria bloqueada** se houver transações vinculadas — mesma lógica.

## Migrations

- Executar `makemigrations` e `migrate` após qualquer alteração em models.
- Fazer backup do `db.sqlite3` antes de migrations destrutivas.

## Restrições das sprints iniciais

- Não implementar Docker.
- Não implementar testes automatizados.

Estas funcionalidades estão no backlog (Sprints 8 e 9).

## Estrutura de arquivos por app

```
app_name/
├── __init__.py
├── admin.py
├── apps.py
├── forms.py       # quando necessário
├── models.py
├── signals.py     # quando necessário
├── urls.py
├── views.py
└── migrations/
```
