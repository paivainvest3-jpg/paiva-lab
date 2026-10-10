# Family Finance Copilot

> Projeto pessoal real · versão pública com dados 100% sintéticos

## Problema

Controle financeiro doméstico costuma quebrar por dois motivos: a planilha vira um arquivo passivo e a pessoa precisa lembrar manualmente o que está parcelado, pago, previsto ou comprometido nos próximos meses.

Este projeto transforma uma planilha financeira em uma base operacional consultável por IA.

## Estrutura real do sistema

A fonte de verdade é um Google Sheets estruturado em abas independentes:

- `Painel` — visão consolidada;
- `Entradas` — renda prevista e recebida;
- `Despesas` — uma linha por gasto, competência, responsável, meio e status;
- `Parcelas` — cadastro do compromisso, parcela atual, próxima competência e saldo de parcelas;
- `Contas Fixas` — referências mensais e variáveis;
- `Histórico 2026` — consolidação histórica;
- `Listas` — apoio a categorias/validações;
- `Instruções IA` — contexto operacional para uso assistido.

## Camada de IA

A IA não substitui a planilha. Ela atua como camada de consulta e decisão:

```text
Pergunta em linguagem natural
        ↓
Leitura das abas relevantes
        ↓
Normalização / prevenção de dupla contagem
        ↓
Cenário financeiro
        ↓
Explicação + projeção + possíveis cortes
```

Exemplos de uso:

- “Se a fatura ficar limitada a X, quanto sobra no mês?”
- “Qual gasto é recorrente e cortável?”
- “Quais parcelas acabam no próximo mês?”
- “Quanto do orçamento sai do salário e quanto sai do benefício alimentação?”
- “Se eu adicionar um custo fixo, como muda a projeção?”

## Decisões de engenharia

### 1. Separar fonte de verdade e inteligência
O Google Sheets continua sendo o ledger. A IA lê e interpreta; não precisa manter uma cópia paralela do saldo.

### 2. Evitar dupla contagem
Um cartão pode conter parcelas, assinaturas e despesas variáveis. A projeção precisa distinguir “fatura total” de itens já incluídos nela.

### 3. Competência > memória
Parcelas futuras são materializadas por competência, reduzindo dependência de lembrar manualmente de compromissos.

### 4. Cenários são explícitos
A IA diferencia valor previsto, realizado, pago, fixo, variável, reserva e benefício externo ao salário.

## O que este case demonstra

- modelagem de dados para finanças pessoais;
- Google Sheets como backend operacional leve;
- leitura estruturada por IA;
- análise de cenários;
- prevenção de inconsistência e dupla contagem;
- linguagem natural como interface para planejamento financeiro.

## Demo pública

Abra [`demo.html`](./demo.html). Ela usa somente dados fictícios e roda 100% no navegador.
