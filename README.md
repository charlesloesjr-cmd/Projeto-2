# Projeto 2 — API Pix e Automação de Testes

Projeto de estudos e portfólio na área de **Quality Assurance (QA)**, desenvolvido com Python, Playwright, Pytest e FastAPI.

O projeto consiste na criação de uma API Pix simulada e na implementação de testes automatizados de interface e API, com foco na validação de regras de negócio, identificação de falhas e documentação dos resultados.

O objetivo é demonstrar conhecimentos práticos em testes funcionais, testes positivos e negativos, automação, organização de cenários e integração contínua.

## Tecnologias utilizadas

- **Python 3.14.7** — linguagem utilizada no desenvolvimento e execução local.
- **Playwright** — automação de testes de interface.
- **Pytest** — estrutura e execução dos testes automatizados.
- **FastAPI** — desenvolvimento da API simulada.
- **HTTPX** — suporte aos testes da API.
- **Pydantic** — validação dos dados recebidos pela API.
- **Uvicorn** — servidor para execução da API.
- **Pytest-HTML** — geração de relatórios de execução.
- **Git e GitHub** — versionamento e hospedagem do projeto.
- **GitHub Actions** — execução automatizada dos testes em pipeline CI.

## Estrutura do projeto

```text
Projeto-2/
│
├── .github/
│   └── workflows/
│       └── playwright.yml
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

## API Pix simulada

A API foi desenvolvida utilizando FastAPI e contempla as seguintes funcionalidades:

- Recebimento de solicitações de transferência Pix.
- Normalização da chave Pix.
- Validação simplificada de CNPJ alfanumérico.
- Verificação de valores positivos.
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

**Observação:** a API possui finalidade exclusivamente educacional. A validação do CNPJ alfanumérico utiliza uma implementação simplificada para os cenários do projeto. Não representa uma validação oficial da Receita Federal e não realiza transferências financeiras reais nem integração com instituições bancárias.

## Cenários de testes automatizados

### Testes de interface — Playwright

Os testes de interface utilizam o padrão **Page Object Model (POM)**, separando os elementos e ações das páginas da implementação dos cenários de teste.

| ID | Cenário | Validação |
|---|---|---|
| UI-001 | Realizar login com sucesso | Acesso à aplicação |
| UI-002 | Realizar transferência Pix | Confirmação da transação, saldo e extrato |

A aplicação utilizada nos testes de interface é o SimulaBank:

https://leogcarvalho.github.io/simulabank/login.html

### Testes de API — Pytest e FastAPI TestClient

| ID | Cenário | Resultado esperado |
|---|---|---|
| API-001 | Realizar Pix com dados válidos | HTTP 200 |
| API-002 | Bloquear transferência acima do limite | HTTP 403 |
| API-003 | Rejeitar transferência com valor zero | HTTP 400 |
| API-004 | Rejeitar CNPJ inválido | HTTP 400 |
| API-005 | Rejeitar destinatário não cadastrado | HTTP 404 |

Os testes de API verificam as respostas da aplicação conforme as regras de negócio implementadas.

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/charlesloesjr-cmd/Projeto-2.git
```

Acessar a pasta:

```bash
cd Projeto-2
```

### 2. Criar e ativar o ambiente virtual

No Windows PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Instalar as dependências

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Instalar o navegador Chromium:

```powershell
python -m playwright install chromium
```

### 4. Executar a API simulada

Para iniciar a API localmente:

```powershell
python -m uvicorn main:app --reload
```

A API ficará disponível em:

http://127.0.0.1:8000

Documentação interativa Swagger:

http://127.0.0.1:8000/docs

**Importante:** os testes automatizados atuais utilizam o TestClient para a API, portanto não é necessário manter o servidor Uvicorn em execução para rodar a suíte de testes.

### 5. Executar os testes automatizados

```powershell
python -m pytest -v
```

### 6. Gerar relatório HTML

Para executar os testes e gerar o relatório:

```powershell
python -m pytest -v --html=reports/relatorio.html --self-contained-html
```

Para abrir o relatório no navegador:

```powershell
start .\reports\relatorio.html
```

## Integração contínua — GitHub Actions

O projeto utiliza **GitHub Actions** para automatizar a execução dos testes.

O workflow está configurado para executar automaticamente quando ocorre:

- Push na branch `main`.
- Pull Request direcionado à branch `main`.

Durante a execução, o pipeline realiza as seguintes etapas:

1. Obtém o código do repositório.
2. Configura o ambiente Python.
3. Instala as dependências.
4. Instala os navegadores necessários para o Playwright.
5. Executa os testes automatizados.
6. Gera o relatório HTML.
7. Disponibiliza o relatório como artefato para download.

O ambiente de CI utiliza Python 3.13, enquanto o desenvolvimento local foi realizado com Python 3.14.7.

As execuções podem ser acompanhadas pela aba **Actions** do GitHub:

https://github.com/charlesloesjr-cmd/Projeto-2/actions

O relatório HTML pode ser baixado na seção **Artifacts** de cada execução do pipeline.

## Resultados dos testes

### Execução local

**Última execução local registrada: 11/11/2026**

| Indicador | Resultado |
|---|---:|
| Total de testes | 7 |
| Aprovados | 7 |
| Reprovados | 0 |
| Taxa de aprovação | 100% |

### GitHub Actions

**Execução registrada: 16/11/2026**

- Pipeline finalizado com sucesso.
- Job `test` aprovado.
- Relatório HTML gerado e disponibilizado como artefato.

Os resultados acima correspondem às execuções registradas nas respectivas datas e não representam uma garantia de aprovação em execuções futuras.

## Conhecimentos demonstrados

- Automação de testes de interface com Playwright.
- Automação de testes de API.
- Desenvolvimento e validação de regras de negócio.
- Testes funcionais e regressivos.
- Validação de cenários positivos e negativos.
- Verificação de códigos e respostas HTTP.
- Organização de testes com Pytest.
- Aplicação do padrão Page Object Model.
- Utilização de Python e ferramentas do ecossistema de QA.
- Versionamento de código com Git e GitHub.
- Integração contínua com GitHub Actions.
- Geração e documentação de relatórios de testes.


## Evidências dos testes

As evidências demonstram a execução dos testes funcionais de interface e as validações da API Pix simulada.

### Testes de interface — Playwright

- [Login realizado com sucesso](evidencias/login/login_sucesso.png)
- [Transferência Pix realizada](evidencias/pix/pix_realizado.png)
- [Validação do extrato Pix](evidencias/pix/pix_extrato.png)

### Testes de API — Swagger

- [Evidências da API em PDF](evidencias/api/Swagger.pdf)
- [Evidências da API em Word](evidencias/api/Swagger.docx)


## Autor

Projeto desenvolvido para fins de aprendizado, prática e construção de portfólio profissional na área de Quality Assurance e Automação de Testes.