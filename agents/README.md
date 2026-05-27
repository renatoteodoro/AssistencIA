# Agentes de IA — AssistencIA

Este diretório define os agentes de IA especializados no desenvolvimento do projeto. Cada agente tem um papel claro no time e deve ser acionado para tarefas dentro de sua especialidade.

---

## Índice de Agentes

| Agente | Arquivo | Especialidade |
|---|---|---|
| Backend Engineer | [backend.md](backend.md) | Django — models, views, forms, URLs, signals, migrations |
| Frontend Engineer | [frontend.md](frontend.md) | Django Template Language + TailwindCSS + design system |
| QA Engineer | [qa.md](qa.md) | Testes via Playwright — verificação funcional e visual |

---

## Quando usar cada agente

### Backend Engineer
Use para tarefas que envolvem código Python/Django:
- Criar ou alterar models e executar migrations
- Implementar views (CBVs), forms e URLs
- Criar signals em `signals.py`
- Registrar models no admin
- Qualquer lógica de negócio (isolamento por usuário, guards de exclusão, filtros de queryset)

### Frontend Engineer
Use para tarefas que envolvem templates e UI:
- Criar ou alterar templates HTML com DTL
- Aplicar classes TailwindCSS conforme o design system do projeto
- Implementar componentes visuais (cards, formulários, badges, sidebar, layout)
- Garantir responsividade e dark mode
- Exibir mensagens de erro do Django com estilo correto

### QA Engineer
Use para verificar que o sistema funciona como esperado:
- Após implementar uma sprint ou feature, acionar o QA para validar o fluxo completo
- Verificar se a UI está correta visualmente (design system, cores, tipografia)
- Identificar bugs funcionais e reportar com detalhes (URL, ação, comportamento esperado vs. observado)
- Validar isolamento de dados entre usuários

---

## Fluxo de trabalho recomendado

```
Backend Engineer → Frontend Engineer → QA Engineer
```

1. O **Backend** implementa models, views e URLs.
2. O **Frontend** cria os templates que consomem essas views.
3. O **QA** acessa o sistema pelo navegador (via Playwright) e valida o resultado.
