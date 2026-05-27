# Design System

O design usa TailwindCSS com tema escuro como padrão e suporte a modo claro via classe `dark`.

## Paleta de Cores

| Token | Dark Mode | Light Mode | Classe Tailwind |
|---|---|---|---|
| Background | `#0f172a` (slate-950) | `#f8fafc` (slate-50) | `bg-slate-950` |
| Surface / Card | `#1e293b` (slate-800) | `#ffffff` | `bg-slate-800` |
| Border | `#334155` (slate-700) | `#e2e8f0` (slate-200) | `border-slate-700` |
| Primária | `#6366f1` (indigo-500) | `#4f46e5` (indigo-600) | `bg-indigo-500` |
| Primária hover | `#4f46e5` (indigo-600) | `#4338ca` (indigo-700) | `hover:bg-indigo-600` |
| Acento | `#22d3ee` (cyan-400) | `#0891b2` (cyan-600) | `text-cyan-400` |
| Sucesso | `#34d399` (emerald-400) | `#059669` (emerald-600) | `text-emerald-400` |
| Perigo | `#f87171` (red-400) | `#dc2626` (red-600) | `text-red-400` |
| Texto principal | `#f1f5f9` (slate-100) | `#0f172a` (slate-950) | `text-slate-100` |
| Texto secundário | `#94a3b8` (slate-400) | `#475569` (slate-600) | `text-slate-400` |

**Gradiente de destaque (hero/header):**
```
bg-gradient-to-br from-indigo-500 via-purple-600 to-cyan-500
```

## Tipografia

Fonte principal: **Inter** (Google Fonts). Monospace: **JetBrains Mono**.

```html
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
```

| Uso | Tailwind |
|---|---|
| Títulos h1–h2 | `font-bold tracking-tight text-3xl` |
| Subtítulos h3 | `font-semibold text-xl` |
| Corpo | `text-base font-normal` |
| Labels | `text-sm font-medium` |
| Monospace | `font-mono text-sm` |

## Componentes

### Botões

```html
<!-- Primário -->
<button class="bg-indigo-600 hover:bg-indigo-700 text-white font-semibold px-4 py-2 rounded-lg transition-colors duration-200">
  Salvar
</button>

<!-- Secundário (outline) -->
<button class="border border-slate-600 hover:border-indigo-500 text-slate-300 hover:text-indigo-400 font-medium px-4 py-2 rounded-lg transition-colors duration-200">
  Cancelar
</button>

<!-- Perigo -->
<button class="bg-red-600 hover:bg-red-700 text-white font-semibold px-4 py-2 rounded-lg transition-colors duration-200">
  Excluir
</button>
```

### Inputs e Formulários

```html
<!-- Label -->
<label class="block text-sm font-medium text-slate-300 mb-1">Nome</label>

<!-- Input -->
<input type="text" class="w-full bg-slate-700 border border-slate-600 text-slate-100 placeholder-slate-400 rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent transition-all duration-200">

<!-- Select -->
<select class="w-full bg-slate-700 border border-slate-600 text-slate-100 rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-indigo-500">
  <option>Opção</option>
</select>

<!-- Erro inline -->
<p class="text-red-400 text-xs mt-1">Este campo é obrigatório.</p>
```

### Card

```html
<div class="bg-slate-800 border border-slate-700 rounded-xl p-5 shadow-lg">
  <!-- conteúdo -->
</div>
```

### Layout Autenticado

```html
<div class="min-h-screen bg-slate-950 flex">
  <aside class="w-64 bg-slate-900 border-r border-slate-700 flex-shrink-0">
    <!-- sidebar -->
  </aside>
  <main class="flex-1 p-6 overflow-y-auto">
    <!-- conteúdo -->
  </main>
</div>
```

### Item de Menu (Sidebar)

```html
<a href="{% url 'dashboard' %}"
   class="flex items-center gap-3 px-3 py-2 rounded-lg text-slate-300 hover:bg-slate-800 hover:text-indigo-400 transition-colors duration-200
          {% if request.resolver_match.url_name == 'dashboard' %}bg-slate-800 text-indigo-400{% endif %}">
  Dashboard
</a>
```

### Badges de Tipo de Transação

```html
<!-- Receita -->
<span class="inline-flex items-center px-2 py-0.5 rounded text-xs font-medium bg-emerald-900 text-emerald-300">Receita</span>

<!-- Despesa -->
<span class="inline-flex items-center px-2 py-0.5 rounded text-xs font-medium bg-red-900 text-red-300">Despesa</span>
```
