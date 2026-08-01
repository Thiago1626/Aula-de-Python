# 📦 Sistema de Controle de Produtos

Sistema web moderno e funcional para gerenciamento de estoque de produtos, desenvolvido com HTML, CSS e JavaScript puro.

## 🚀 Funcionalidades

### 1. **Cadastrar Produto**
- Adicione novos produtos com nome, preço e quantidade
- Validação de campos obrigatórios
- Formatação automática de valores

### 2. **Listar Produtos**
- Visualização em tabela organizada
- Exibição de nome, preço, quantidade e valor total
- Design responsivo e limpo

### 3. **Buscar Produto**
- Busca em tempo real
- Filtragem instantânea por nome
- Botão para limpar busca

### 4. **Calcular Valor Total do Estque**
- Dashboard com estatísticas atualizadas automaticamente
- Total de produtos cadastrados
- Valor total do estoque (R$)
- Quantidade total de itens

### 5. **Excluir Produto**
- Modal de confirmação para exclusão
- Feedback visual de sucesso/erro
- Atualização automática da lista

## 🎨 Características do Design

- **Interface Moderna**: Gradientes, sombras e animações suaves
- **Totalmente Responsivo**: Adapta-se a desktop, tablet e mobile
- **Animações**: Efeitos de entrada e transições elegantes
- **Feedback Visual**: Notificações toast para ações do usuário
- **Ícones Emoji**: Interface mais amigável e intuitiva

## 💾 Persistência de Dados

Os dados são salvos automaticamente no **localStorage** do navegador, garantindo que as informações persistam mesmo após fechar a página.

## 🛠️ Tecnologias Utilizadas

- **HTML5**: Estrutura semântica
- **CSS3**: 
  - CSS Grid e Flexbox para layout
  - Variáveis CSS para tema consistente
  - Animações e transições
  - Media queries para responsividade
- **JavaScript (Vanilla)**:
  - Manipulação do DOM
  - localStorage para persistência
  - Event listeners para interatividade
  - Funções assíncronas

## 📱 Responsividade

O sistema se adapta automaticamente a diferentes tamanhos de tela:

- **Desktop** (> 968px): Layout em duas colunas
- **Tablet** (600px - 968px): Layout em coluna única
- **Mobile** (< 600px): Interface otimizada para telas pequenas

## 🎯 Como Usar

1. Abra o arquivo `sistema-controle-produtos.html` em um navegador moderno
2. **Cadastrar Produto**: Preencha o formulário à esquerda e clique em "Cadastrar Produto"
3. **Visualizar Produtos**: Os produtos aparecem automaticamente na tabela à direita
4. **Buscar Produto**: Digite o nome no campo de busca para filtrar
5. **Excluir Produto**: Clique no botão "Excluir" na linha do produto desejado
6. **Acompanhar Estatísticas**: Verifique o dashboard no topo da página

## 📊 Estrutura do Código

```
sistema-controle-produtos.html
├── <head>
│   ├── Meta tags (charset, viewport)
│   └── <style> (CSS embutido)
│       ├── Variáveis CSS
│       ├── Reset e base
│       ├── Layout (container, grid)
│       ├── Componentes (cards, forms, tabelas)
│       ├── Modal e Toast
│       ├── Animações
│       └── Media Queries
├── <body>
│   ├── Header
│   ├── Dashboard (estatísticas)
│   ├── Formulário de Cadastro
│   ├── Lista de Produtos
│   ├── Modal de Exclusão
│   └── Toast Notification
└── <script> (JavaScript embutido)
    ├── Gerenciamento de estado
    ├── Funções CRUD
    ├── Manipulação do DOM
    ├── Event Listeners
    └── Inicialização
```

## 🔧 Funcionalidades JavaScript

### Estado Global
```javascript
let produtos = [] // Array de produtos
let produtoParaExcluir = null // Produto selecionado para exclusão
```

### Funções Principais
- `salvarProdutos()` - Salva no localStorage
- `atualizarDashboard()` - Atualiza estatísticas
- `cadastrarProduto()` - Adiciona novo produto
- `listarProdutos()` - Renderiza tabela de produtos
- `buscarProduto()` - Filtra produtos por nome
- `abrirModalExclusao()` - Abre modal de confirmação
- `confirmarExclusao()` - Remove produto da lista

## 🎨 Paleta de Cores

- **Primária**: #6366f1 (Índigo)
- **Secundária**: #8b5cf6 (Violeta)
- **Sucesso**: #10b981 (Verde)
- **Perigo**: #ef4444 (Vermelho)
- **Fundo**: Gradiente roxo/azul

## ✨ Recursos Especiais

- ✅ Sem necessidade de instalação ou dependências
- ✅ Funciona offline após carregar
- ✅ Dados salvos localmente no navegador
- ✅ Interface intuitiva e fácil de usar
- ✅ Código limpo e bem organizado
- ✅ Comentários explicativos

## 📝 Notas

- Os dados são armazenados no localStorage do navegador
- Para limpar todos os dados, use as ferramentas de desenvolvedor do navegador
- Recomendado usar navegadores modernos (Chrome, Firefox, Edge, Safari)

## 👨‍💻 Desenvolvimento

Sistema desenvolvido como projeto educacional baseado no sistema Python `ex5.py`, convertido para uma interface web moderna e interativa.

---

**Versão**: 1.0.0  
**Data**: Janeiro 2026  
**Tipo**: Aplicação Web Single Page (SPA)
