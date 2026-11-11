# Projeto 2 — API Pix e Automação de Testes

Projeto de estudos e portfólio na área de **Quality Assurance (QA)**, com desenvolvimento de uma API Pix simulada e automação de testes funcionais de interface e API utilizando Python, Playwright, FastAPI e Pytest.

O objetivo é demonstrar conhecimentos em testes funcionais, validação de regras de negócio, testes positivos e negativos, automação e documentação de resultados.

## Tecnologias utilizadas

- **Python 3.14.7** — linguagem de programação.
- **Playwright** — automação de testes de interface.
- **Pytest** — estrutura e execução dos testes automatizados.
- **FastAPI** — desenvolvimento da API simulada.
- **HTTPX** — suporte aos testes da API.
- **Pydantic** — validação dos dados recebidos pela API.
- **Uvicorn** — servidor para execução da API.
- **Pytest-HTML** — geração de relatórios de execução.

## Estrutura do projeto

```text
Projeto 2/
│
├── .github/
│
├── pages/
│   ├── common_page.py
│   ├── login_page.py
│   ├── home_page.py
│   └── pix_page.py
│
├── tests/
│   ├── test_001_login.py
│   ├── test_002_pix_realizado.py
│   └── test_api_pix.py
│
├── reports/
│   └── relatorio.html
│
├── main.py
├── conftest.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Funcionalidades da API Pix

A API foi desenvolvida com FastAPI e disponibiliza as seguintes funcionalidades:

- Recebimento de solicitações de transferência Pix.
- Normalização da chave Pix.
- Validação simplificada de CNPJ alfanumérico.
- Verificação de valor positivo.
- Controle de limite máximo de transferência de R$ 3.000,00.
- Consulta de destinatário em uma base simulada.
- Retorno de mensagens e códigos HTTP conforme o resultado da operação.

### Endpoint

**POST /pix**

Exemplo de requisição:

```json
{
  "chave_pix": "12ABC34501DE35",
  "valor": 100.00
}
```

Exemplo de resposta:

```json
{
  "status": "AUTORIZADO",
  "mensagem": "Pix realizado com sucesso!",
  "destinatario": "Empresa Exemplo Ltda.",
  "chave_pix": "12ABC34501DE35",
  "valor": "100.00"
}
```

### Regras de negócio validadas

| Regra | Código HTTP |
|---|---:|
| Transferência autorizada | 200 |
| CNPJ inválido | 400 |
| Valor igual ou inferior a zero | 400 |
| Valor acima do limite permitido | 403 |
| Destinatário não cadastrado | 404 |

**Observação:** esta é uma API educacional e simulada. A validação do CNPJ alfanumérico utiliza uma implementação simplificada para os cenários do projeto. Não representa uma validação oficial da Receita Federal e não realiza transferências financeiras reais ou integração com instituições bancárias.

## Cenários de testes automatizados

### Testes de interface — Playwright

| ID | Cenário | Resultado |
|---|---|---|
| UI-001 | Realizar login com sucesso | Aprovado |
| UI-002 | Realizar transferência Pix e validar saldo e extrato | Aprovado |

Os testes de interface utilizam o padrão Page Object Model (POM), separando os elementos e ações das páginas da implementação dos cenários de teste.

A aplicação utilizada nos testes de interface é o SimulaBank: https://leogcarvalho.github.io/simulabank/login.html

### Testes de API — Pytest e FastAPI TestClient

| ID | Cenário | Resultado esperado |
|---|---|---|
| API-001 | Realizar Pix com dados válidos | HTTP 200 |
| API-002 | Bloquear transferência acima do limite | HTTP 403 |
| API-003 | Rejeitar transferência com valor zero | HTTP 400 |
| API-004 | Rejeitar CNPJ inválido | HTTP 400 |
| API-005 | Rejeitar destinatário não cadastrado | HTTP 404 |

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone URL_DO_REPOSITORIO
```

Entre na pasta do projeto:

```bash
cd "Projeto 2"
```

### 2. Criar e ativar o ambiente virtual

Windows PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Instalar as dependências

```powershell
python -m pip install -r requirements.txt
```

Instalar o navegador Chromium:

```powershell
python -m playwright install chromium
```

### 4. Executar a API

```powershell
python -m uvicorn main:app --reload
```

A API ficará disponível em:

http://127.0.0.1:8000

Documentação interativa Swagger:

http://127.0.0.1:8000/docs

### 5. Executar os testes automatizados

Com a API não sendo necessária para os testes automatizados atuais, execute a suíte completa em outro terminal:

```powershell
python -m pytest -v
```

### 6. Gerar relatório HTML

```powershell
python -m pytest -v --html=reports/relatorio.html --self-contained-html
```

Para abrir o relatório no navegador:

```powershell
start .\reports\relatorio.html
```

## Resultados da execução

**Última execução registrada: 11/11/2026**

| Indicador | Resultado |
|---|---:|
| Total de testes | 7 |
| Aprovados | 7 |
| Reprovados | 0 |
| Ignorados | 0 |

**Taxa de aprovação: 100%.**

Relatório HTML disponível na pasta `reports/relatorio.html`.

## Conhecimentos demonstrados

- Automação de testes de interface com Playwright.
- Automação de testes de API.
- Desenvolvimento e validação de regras de negócio.
- Testes funcionais e regressivos.
- Validação de cenários positivos e negativos.
- Verificação de códigos e respostas HTTP.
- Organização de testes com Pytest.
- Aplicação do padrão Page Object Model.
- Geração e documentação de relatórios de testes.
- Utilização de Python e ferramentas do ecossistema de QA.

## Autor

Projeto desenvolvido para fins de aprendizado, prática e construção de portfólio profissional na área de Quality Assurance e Automação de Testes.