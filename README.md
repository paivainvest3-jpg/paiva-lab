# PAIVA LAB // AI · RISK · AUTOMATION

Portfólio profissional de Paiva focado em engenharia aplicada a risco, fraude, IA e automação.

## O que este repositório prova

- capacidade de transformar problemas ambíguos em sistemas executáveis;
- uso de LLMs com guardrails, tool calling e trilha de auditoria;
- modelagem de risco com segmentação, clustering, scoring e monitoramento;
- engenharia local-first e persistência robusta em produto mobile;
- automação de processos com APIs, Python, eventos e validações.

## Cases

1. **Fold AI** — assistente pessoal Android com Cloudflare Workers AI, Tasker, AutoRemote, D1 e PWA.
2. **Risk Intelligence Engine** — case sanitizado e reproduzível com dados sintéticos, clustering e score de risco.
3. **Aureon** — Life RPG local-first com Android/Capacitor, SQLite, IA local e arquitetura orientada a eventos.
4. **Family Finance Copilot** — Google Sheets + IA para consultas, projeções e análise de cenários financeiros, com demo sintética.
5. **Personal Workspace** — workspace web pessoal; case público focado em produto/UX e privacidade.
6. **OpsFlow AI** — lab demonstrativo de automação operacional auditável.
7. **Document Intake Agent** — lab demonstrativo de triagem de documentos com structured output, abstention e human-in-the-loop.

## Transparência

Os projetos `Fold AI`, `Aureon`, `Family Finance Copilot` e `Personal Workspace` são projetos pessoais reais. `Risk Intelligence Engine` é uma reconstrução sanitizada de padrões de engenharia e modelagem usados em trabalho com risco, usando apenas dados sintéticos e sem regras, dados ou propriedade intelectual de empregadores. Os demais itens marcados como **Lab demonstrativo** foram criados para demonstrar capacidades técnicas e não devem ser apresentados como projetos de cliente.

## Rodar o site

O site é estático e não precisa de build:

```bash
python -m http.server 8080
```

Abra `http://localhost:8080`.

## Publicação recomendada

- Repositório público no GitHub para prova técnica.
- Deploy contínuo no Cloudflare Pages/Workers via integração Git.
- Domínio próprio opcional quando o posicionamento estiver validado.

## Antes de publicar

- adicionar links reais de LinkedIn/GitHub/contato;
- revisar nomes de tecnologias e qualquer informação que possa ser confidencial;
- adicionar screenshots próprias de Fold AI e Aureon em `assets/`;
- trocar qualquer métrica demonstrativa por resultados reais somente quando puder ser comprovada.
