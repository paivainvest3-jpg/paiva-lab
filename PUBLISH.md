# Publicação — caminho recomendado

## Arquitetura de presença
**GitHub público → Cloudflare deploy → LinkedIn/marketplaces apontando para o site**

O GitHub funciona como prova técnica e histórico. A Cloudflare funciona como vitrine e deploy. Para um portfólio estático como este, não é necessário framework nem etapa de build.

## 1. Criar o repositório no GitHub
Nome recomendado: `paiva-lab`

Descrição:
> AI, risk, fraud and automation portfolio — agents, analytics, mobile systems and reliable workflows.

Deixe o repositório público.

No terminal, dentro desta pasta:

```bash
git init
git add .
git commit -m "feat: launch Paiva Lab portfolio"
git branch -M main
git remote add origin https://github.com/SEU-USUARIO/paiva-lab.git
git push -u origin main
```

## 2. Cloudflare
Opção simples: conectar o repositório à Cloudflare e configurar deploy do conteúdo estático da raiz.

Configuração do site atual:
- branch: `main`
- site estático: sim
- arquivo inicial: `index.html`
- build: nenhum necessário
- output: raiz do repositório

## 3. Ordem de links públicos
1. Site do portfólio
2. LinkedIn
3. GitHub
4. 99Freelas
5. Workana
6. Upwork quando o perfil em inglês estiver pronto

## 4. Repositórios futuros
Depois que a vitrine estiver publicada, separar os projetos mais fortes em repositórios próprios:
- `fold-ai-architecture` — versão pública/sanitizada da arquitetura, sem secrets;
- `risk-intelligence-lab` — demo reproduzível com dados sintéticos;
- `aureon-public-case` — case/arquitetura e screenshots, sem expor código privado do produto;
- `family-finance-copilot` — arquitetura e demo sintética do sistema financeiro;
- `nharryme-workspace-case` — case de produto/UX com screenshots sanitizados;
- `reliable-agent-labs` — labs de automação e document intake.

## 5. Segurança antes do push
Nunca publicar:
- tokens e chaves;
- AutoRemote key / app token;
- dados reais de usuário/cliente/empresa;
- regras e thresholds proprietários;
- URLs internas;
- nomes de tabelas/infra que revelem informação corporativa sensível;
- dumps SQLite reais.

Faça busca por `token`, `secret`, `key`, `password`, `bearer`, `.env` antes de qualquer push de projetos existentes.
