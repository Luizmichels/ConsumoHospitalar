# MedStock AI — Contexto Completo do Projeto

> **Documento de referência para desenvolvimento.**
> Sistema de análise preditiva de consumo de insumos hospitalares.
> TCC — Engenharia de Software, Católica SC. Orientador: Diogo Vinícius Winck.

---

## 1. Visão Geral do Projeto

**Nome:** MedStock AI  
**Tagline:** Gestão Inteligente de Estoques  
**Tipo:** Aplicação web SaaS multitenant  
**Objetivo:** Coletar e analisar dados históricos de consumo hospitalar, aplicar modelos de Machine Learning para geração de previsões de demanda e disponibilizar um painel analítico para gestores hospitalares.

### Problema

No setor hospitalar, os custos de suprimentos podem representar entre 20% e 46% dos gastos operacionais. A ausência de ferramentas preditivas gera dois problemas recorrentes:
- **Excesso de estoque** — desperdício por vencimento de materiais
- **Ruptura de estoque** — falta de insumos críticos comprometendo o atendimento

### Diferencial

Solução especializada no contexto hospitalar com Machine Learning para previsão de demanda, interface acessível para não técnicos, classificação ABC dos itens e exportação de relatórios. Preenche a lacuna entre soluções enterprise complexas (GTPlan, Bionexo) e plataformas de ML voltadas ao varejo (Slimstock, o9 Solutions).

---

## 2. Stack Tecnológica

| Camada | Tecnologia |
|---|---|
| Front-end | React + Next.js + Node.js |
| Back-end | Python + FastAPI |
| ORM | SQLAlchemy |
| Banco de dados | PostgreSQL |
| ML | Scikit-learn + Statsmodels (ARIMA, Holt-Winters) |
| Autenticação | JWT (python-jose) + bcrypt (passlib) |
| Exportação | ReportLab (PDF) + OpenPyXL (Excel) |
| Dados | Pandas + NumPy |

---

## 3. Arquitetura — Visão Geral

O sistema é uma arquitetura **multitenant** onde cada hospital (empresa) tem seus dados completamente isolados pelo campo `empresa_id` presente em todas as tabelas operacionais.

### Containers
- **Aplicação Web** (React/Next.js) — interface do usuário
- **API REST** (FastAPI) — orquestra todos os módulos
- **Serviço de ML** (Scikit-learn/Statsmodels) — pipeline de treinamento e previsão
- **Banco de Dados** (PostgreSQL) — persistência

### Módulos da API REST
1. **Autenticação e Controle de Acesso** — JWT, sessões, perfis por empresa
2. **Importação de Dados** — upload CSV/Excel e integração via API
3. **Validação e Tratamento** — pipeline de qualidade dos dados
4. **Treinamento e Predição** — pipeline de ML, métricas RMSE/MAE/MAPE
5. **Dashboard** — KPIs, gráficos, classificação ABC
6. **Exportação de Relatórios** — PDF e Excel
7. **Gestão de Usuários** — CRUD de usuários por empresa (Administrador)
8. **Gestão de Empresas** — exclusivo do Super Admin
9. **API REST** — FastAPI com documentação automática em /docs
10. **Camada de Persistência** — PostgreSQL + SQLAlchemy

---

## 4. Perfis de Acesso

| Perfil | Descrição | Acesso |
|---|---|---|
| **Super Admin** | Gerencia toda a plataforma | Gestão de Hospitais, aprovação de solicitações. Credenciais via variável de ambiente, não ficam no banco |
| **Administrador** | Gerencia a empresa/hospital | Todas as telas da empresa: Dashboard, Importar Dados, Previsões, Exportar Relatório, Gestão de Usuários |
| **Usuário** | Consulta apenas | Dashboard, Previsões, Exportar Relatório |

---

## 5. Requisitos Funcionais (RF)

| Código | Descrição |
|---|---|
| RF01 | Cadastro e autenticação de usuários com perfis distintos (Administrador e Usuário) |
| RF02 | Importação de bases históricas de consumo em CSV ou Excel, e integração via API REST com periodicidade configurável |
| RF03 | Visualização dos dados importados em tabelas e gráficos |
| RF04 | Validações automáticas nos dados importados: campos obrigatórios, padronização, nulos, duplicidades, inconsistências de formato, agregação temporal e armazenamento |
| RF05 | Classificação ABC dos itens por padrão de consumo (A = 70%, B = 20%, C = 10% do valor acumulado) |
| RF06 | Pipeline de treinamento de modelos preditivos: ingestão, preparação, engenharia de atributos, treino/validação/teste, avaliação e registro |
| RF07 | Exibição do desempenho dos modelos com métricas RMSE, MAE e MAPE |
| RF08 | Geração de previsões de consumo futuro para materiais e medicamentos |
| RF09 | Painel (dashboard) com gráficos para apoio à tomada de decisão |
| RF10 | Exportação dos resultados em PDF e Excel (.xlsx) |
| RF11 | Retreinamento manual dos modelos com novos dados, mantendo registro de versões |
| RF12 | Mensagem informativa no Dashboard quando não houver dados importados |
| RF13 | Super Admin pode cadastrar, editar e desativar empresas (hospitais) |
| RF14 | Botão de "Solicitar Acesso" na tela de Login com formulário: e-mail, responsável e nome do hospital |
| RF15 | Super Admin pode visualizar, aprovar ou rejeitar solicitações de acesso |
| RF16 | Isolamento total de dados entre empresas |

---

## 6. Requisitos Não Funcionais (RNF)

| Código | Descrição |
|---|---|
| RNF01 | Páginas carregam em até 3 segundos |
| RNF02 | Previsões para até 1.000 itens em no máximo 60 segundos |
| RNF03 | Interface intuitiva para usuários não técnicos |
| RNF04 | Autenticação obrigatória para acesso às funcionalidades restritas |
| RNF05 | Conformidade com LGPD — minimização de dados, sem dados de pacientes |
| RNF06 | Disponível durante o período acadêmico |
| RNF07 | Arquitetura extensível para integração com novas fontes de dados via API |
| RNF08 | Código modular para facilitar manutenção |
| RNF09 | Logs de execução, erros e falhas para rastreabilidade |
| RNF10 | Compatível com os principais navegadores |
| RNF11 | Comunicação cliente-servidor via HTTPS |

---

## 7. Regras de Negócio (RN)

| Código | Categoria | Descrição |
|---|---|---|
| RN01 | Controle de Acesso | Três perfis: Super Admin (plataforma), Administrador (empresa), Usuário (consulta) |
| RN02 | Controle de Acesso | Só Administrador importa dados, restrito à sua empresa |
| RN03 | Validação | Colunas obrigatórias no arquivo: código do item, descrição, data, quantidade, local de estoque |
| RN04 | Exportação | Exportação disponível para todos os perfis em PDF e Excel |
| RN05 | Classificação ABC | A = 70%, B = 20%, C = 10% do valor acumulado de consumo |
| RN06 | Modelo Preditivo | Mínimo de 3 meses de histórico válido para gerar previsões |
| RN07 | Dashboard | Mensagem informativa quando não há dados importados |
| RN08 | Isolamento | Cada empresa acessa apenas seus próprios dados |
| RN09 | Gestão de Empresas | Somente Super Admin cadastra, edita e desativa empresas |
| RN10 | Aprovação | Solicitações ficam com status "pendente" até deliberação do Super Admin |
| RN11 | Super Admin | Credenciais via variável de ambiente, fora do banco de usuários comuns |

---

## 8. Modelo de Dados — Tabelas

### Tabelas do Sistema

```sql
-- Conta do superadministrador (fora do fluxo normal de usuários)
CREATE TABLE super_admins (
    id         SERIAL PRIMARY KEY,
    email      VARCHAR(255) NOT NULL UNIQUE,
    senha_hash VARCHAR(255) NOT NULL,
    criado_em  TIMESTAMP DEFAULT NOW()
);

-- Solicitações de acesso de novos hospitais (via formulário do login)
CREATE TABLE solicitacoes_acesso (
    id            SERIAL PRIMARY KEY,
    email         VARCHAR(255) NOT NULL,
    nome_contato  VARCHAR(255) NOT NULL,
    nome_hospital VARCHAR(255) NOT NULL,
    status        VARCHAR(20) NOT NULL DEFAULT 'pendente', -- pendente | aprovado | reprovado
    criado_em     TIMESTAMP DEFAULT NOW()
);

-- Hospitais/clientes cadastrados na plataforma
CREATE TABLE empresas (
    id           SERIAL PRIMARY KEY,
    nome         VARCHAR(255) NOT NULL,
    cnpj         VARCHAR(18)  NOT NULL UNIQUE,
    data_entrada DATE,
    data_saida   DATE,
    ativo        BOOLEAN NOT NULL DEFAULT TRUE,
    criado_em    TIMESTAMP DEFAULT NOW()
);

-- Usuários vinculados a uma empresa
CREATE TABLE usuarios (
    id            SERIAL PRIMARY KEY,
    empresa_id    INTEGER NOT NULL REFERENCES empresas(id),
    nome          VARCHAR(255) NOT NULL,
    email         VARCHAR(255) NOT NULL UNIQUE,
    senha_hash    VARCHAR(255) NOT NULL,
    perfil        VARCHAR(20)  NOT NULL, -- 'admin' | 'usuario'
    ativo         BOOLEAN NOT NULL DEFAULT TRUE,
    criado_em     TIMESTAMP DEFAULT NOW(),
    atualizado_em TIMESTAMP DEFAULT NOW()
);

-- Insumos hospitalares da empresa
CREATE TABLE itens (
    id                SERIAL PRIMARY KEY,
    empresa_id        INTEGER NOT NULL REFERENCES empresas(id),
    codigo            VARCHAR(100) NOT NULL,
    descricao         VARCHAR(255) NOT NULL,
    unidade_medida    VARCHAR(20),
    classificacao_abc CHAR(1), -- A | B | C
    ativo             BOOLEAN NOT NULL DEFAULT TRUE
);

-- Locais físicos de armazenamento
CREATE TABLE locais_estoque (
    id         SERIAL PRIMARY KEY,
    empresa_id INTEGER NOT NULL REFERENCES empresas(id),
    nome       VARCHAR(255) NOT NULL,
    descricao  TEXT
);

-- Histórico de arquivos importados
CREATE TABLE importacoes (
    id                SERIAL PRIMARY KEY,
    empresa_id        INTEGER NOT NULL REFERENCES empresas(id),
    usuario_id        INTEGER NOT NULL REFERENCES usuarios(id),
    tipo              VARCHAR(20),   -- 'csv' | 'excel' | 'api'
    nome_arquivo      VARCHAR(255),
    status            VARCHAR(20),   -- 'processando' | 'concluido' | 'erro'
    total_registros   INTEGER,
    registros_validos INTEGER,
    registros_erros   INTEGER,
    criado_em         TIMESTAMP DEFAULT NOW()
);

-- Registros de consumo histórico
CREATE TABLE consumos (
    id               SERIAL PRIMARY KEY,
    empresa_id       INTEGER NOT NULL REFERENCES empresas(id),
    item_id          INTEGER NOT NULL REFERENCES itens(id),
    local_estoque_id INTEGER NOT NULL REFERENCES locais_estoque(id),
    importacao_id    INTEGER REFERENCES importacoes(id),
    data_consumo     DATE    NOT NULL,
    quantidade       NUMERIC(10,2) NOT NULL
);

-- Modelos de ML treinados
CREATE TABLE modelos_ml (
    id          SERIAL PRIMARY KEY,
    empresa_id  INTEGER NOT NULL REFERENCES empresas(id),
    nome        VARCHAR(255),
    algoritmo   VARCHAR(100), -- 'arima' | 'holt_winters' | 'random_forest' | etc
    versao      INTEGER,
    rmse        NUMERIC(10,4),
    mae         NUMERIC(10,4),
    mape        NUMERIC(10,4),
    status      VARCHAR(20),  -- 'treinando' | 'ativo' | 'inativo'
    treinado_em TIMESTAMP
);

-- Previsões geradas pelos modelos
CREATE TABLE previsoes (
    id                  SERIAL PRIMARY KEY,
    empresa_id          INTEGER NOT NULL REFERENCES empresas(id),
    item_id             INTEGER NOT NULL REFERENCES itens(id),
    modelo_id           INTEGER NOT NULL REFERENCES modelos_ml(id),
    data_referencia     DATE    NOT NULL,
    quantidade_prevista NUMERIC(10,2),
    criado_em           TIMESTAMP DEFAULT NOW()
);
```

---

## 9. Estrutura de Pastas — Back-end

```
backend/
├── app/
│   ├── main.py                  # Inicialização do FastAPI
│   ├── database.py              # Conexão PostgreSQL (SQLAlchemy)
│   ├── dependencies.py          # Injeção de dependências (auth, db session)
│   ├── core/
│   │   ├── config.py            # Variáveis de ambiente (.env)
│   │   ├── security.py          # JWT, bcrypt
│   │   └── exceptions.py        # Exceções customizadas
│   ├── models/                  # Modelos SQLAlchemy
│   │   ├── empresa.py
│   │   ├── usuario.py
│   │   ├── item.py
│   │   ├── consumo.py
│   │   ├── importacao.py
│   │   ├── modelo_ml.py
│   │   ├── previsao.py
│   │   └── local_estoque.py
│   ├── schemas/                 # Schemas Pydantic
│   │   ├── empresa.py
│   │   ├── usuario.py
│   │   ├── importacao.py
│   │   └── previsao.py
│   ├── routers/                 # Endpoints por módulo
│   │   ├── auth.py
│   │   ├── usuarios.py
│   │   ├── empresas.py
│   │   ├── importacoes.py
│   │   ├── previsoes.py
│   │   ├── dashboard.py
│   │   └── exportacoes.py
│   ├── services/                # Regras de negócio
│   │   ├── auth_service.py
│   │   ├── importacao_service.py
│   │   ├── validacao_service.py
│   │   └── exportacao_service.py
│   └── ml/                      # Pipeline de ML
│       ├── pipeline.py
│       ├── preprocessamento.py
│       ├── modelos.py
│       └── avaliacao.py
├── migrations/                  # Alembic
├── tests/
├── .env
├── .env.example
├── requirements.txt
└── Dockerfile
```

---

## 10. Variáveis de Ambiente (.env)

```env
DATABASE_URL=postgresql://usuario:senha@localhost:5432/medstock
SECRET_KEY=sua_chave_secreta_aqui
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
SUPER_ADMIN_EMAIL=admin@medstock.com
SUPER_ADMIN_SENHA=senha_segura_aqui
```

---

## 11. Telas do Sistema

### Telas por perfil

| Tela | Usuário | Administrador | Super Admin |
|---|---|---|---|
| Login | ✓ | ✓ | ✓ |
| Solicitação de Acesso | público | público | público |
| Dashboard | ✓ | ✓ | — |
| Previsões | ✓ | ✓ | — |
| Exportar Relatório | ✓ | ✓ | — |
| Importar Dados | — | ✓ | — |
| Gestão de Usuários | — | ✓ | — |
| Gestão de Hospitais | — | — | ✓ |

### Descrição das Telas

**Login** — Autenticação com e-mail e senha. Botão "Tem interesse em obter o sistema?" redireciona para o formulário de Solicitação de Acesso.

**Solicitação de Acesso** — Formulário público com campos: Responsável pelo Contato, E-mail e Nome da Instituição. Solicitação é registrada com status `pendente`.

**Dashboard** — KPIs, gráficos de consumo mensal, consumo por local de estoque e classificação ABC. Exibe mensagem informativa se não há dados importados.

**Importar Dados** — Upload de CSV/Excel ou configuração de integração via API com periodicidade configurável. Exibe histórico de importações.

**Previsões** — Gráficos de tendência e tabela de itens com previsões de consumo futuro.

**Exportar Relatório** — Seleção de tipo de relatório e exportação em PDF ou Excel.

**Gestão de Usuários** — CRUD de usuários da empresa com definição de perfil de acesso.

**Gestão de Hospitais (Super Admin)** — Painel com 4 KPIs (ativas, pendentes, inativas, total). Tabela com colunas: Responsável, E-mail, Hospital, Status, Ações. Registros `Ativo/Inativo` têm botão "Editar". Registros `Pendente` têm botões "Aprovar" e "Reprovar".

---

## 12. Fluxos de Interação

### Administrador — Importar dados e visualizar Dashboard
1. Login com credenciais
2. Dashboard exibe mensagem de ausência de dados
3. Navega para Importar Dados
4. Faz upload do arquivo CSV
5. Sistema valida automaticamente
6. Importação registrada no histórico
7. Dashboard atualizado com KPIs e gráficos

### Usuário — Consultar previsões
1. Login com credenciais
2. Dashboard com KPIs e gráficos
3. Navega para Previsões
4. Analisa itens com maior consumo previsto

### Super Admin — Aprovar solicitação de acesso
1. Login com credenciais
2. Redireciona para Gestão de Hospitais
3. Visualiza KPIs e identifica pendências
4. Localiza solicitação na tabela
5. Clica em "Aprovar" — status atualizado para Ativo

---

## 13. Fluxos Alternativos

| Código | Condição | Resposta do sistema |
|---|---|---|
| FA01 | Credenciais inválidas no login | Exibe erro, permite nova tentativa |
| FA02 | Arquivo de importação inválido (colunas ausentes) | Rejeita importação, exibe erro detalhado |
| FA03 | Item com menos de 3 meses de histórico | Gera previsão só para itens elegíveis, exibe aviso |
| FA04 | Sessão expirada por inatividade | Encerra sessão e redireciona para login |
| FA05 | Usuário tenta acessar funcionalidade restrita | Bloqueia e exibe mensagem de permissão negada |

---

## 14. Métricas de Sucesso (KPIs)

### Desempenho dos Modelos Preditivos

| Métrica | Descrição | Meta |
|---|---|---|
| MAPE | Erro percentual médio absoluto | < 20% |
| MAE | Erro absoluto médio em unidades | Minimizar vs. baseline |
| RMSE | Raiz do erro quadrático médio | Minimizar vs. baseline |

### Desempenho do Sistema

| Indicador | Meta |
|---|---|
| Tempo de resposta das páginas | Até 3 segundos |
| Tempo de geração de previsões (1.000 itens) | Até 60 segundos |
| Cobertura de itens com previsão | Mínimo 80% dos importados |

---

## 15. Segurança e LGPD

- **Sem dados de pacientes** — o sistema processa apenas dados operacionais de consumo
- **Dados coletados:** código do item, descrição, data, quantidade, local de estoque (operacionais) + nome, e-mail e perfil dos usuários (pessoais)
- **Senhas** armazenadas com bcrypt
- **Comunicação** exclusivamente via HTTPS
- **Direitos LGPD:** acesso, correção e exclusão mediante solicitação ao Administrador

---

## 16. Planejamento

| Marco | Descrição | Prazo |
|---|---|---|
| M1 | Documentação RFC finalizada | 30/04/2026 |
| M2 | Back-end: API REST, importação, validação, persistência | 15/06/2026 |
| M3 | Front-end: todas as telas + integração com API | 05/08/2026 |
| M4 | Pipeline de ML: treinamento, avaliação, métricas | 30/10/2026 |
| M5 | Integração, testes finais e entrega do TCC | 30/11/2026 |

---

## 17. Links do Projeto

- **Figma (protótipo):** https://www.figma.com/design/AhP2PCySRYgYfjRPKHZRTY
- **Repositório:** https://github.com/Luizmichels/MedStock-AI
- **Diagramas (draw.io):** https://app.diagrams.net/?src=about#G11MZcrJfoFZt-voZ4wql40aV1GSZYBvYj
