Projeto 2 — Testes Automatizados com Playwright e Python
Projeto de automação de testes web utilizando Python, Playwright e Pytest. O objetivo é validar fluxos essenciais do SimulaBank, incluindo autenticação e realização de uma transferência via Pix.
Tecnologias utilizadas
- Python — linguagem utilizada para desenvolver os testes.
- Playwright — automação e interação com o navegador.
- Pytest — execução e organização dos testes automatizados.
- pytest-playwright — integração entre Pytest e Playwright.
- GitHub Actions — execução automatizada dos testes em pipeline CI.
- Page Object Model (POM) — organização dos elementos e ações das páginas em classes reutilizáveis.
O workflow do GitHub Actions está configurado para utilizar Python 3.13. Recomenda-se utilizar essa versão localmente para manter o ambiente próximo ao da integração contínua.

Aplicação testada
Os testes são executados no ambiente de demonstração SimulaBank:

https://leogcarvalho.github.io/simulabank/login.html

As credenciais utilizadas atualmente nos testes são dados de demonstração:
- Usuário: user1
- Senha: pass1
Utilize somente o ambiente de demonstração. Não informe credenciais ou dados bancários reais.
Cenários automatizados
Arquivo	Cenário	Validações principais
tests/test_001_login.py	Login com sucesso	Preenchimento das credenciais e exibição da mensagem de boas-vindas.
tests/test_002_pix_realizado.py	Realização de Pix	Login, acesso à opção Fazer Pix, envio da transferência, confirmação de sucesso, retorno à Home, validação do saldo e consulta ao extrato.

Projeto-2/
├── .github/
│   └── workflows/
│       └── playwright.yml
├── pages/
│   ├── common_page.py
│   ├── home_page.py
│   ├── login_page.py
│   └── pix_page.py
├── tests/
│   ├── test_001_login.py
│   └── test_002_pix_realizado.py
├── .gitignore
├── conftest.py
└── requirements.txt
Organização
- pages/: classes Page Object, com elementos e ações de cada página.
- tests/: casos de teste automatizados.
- conftest.py: configuração inicial do navegador e fixtures compartilhadas.
- requirements.txt: dependências Python.
- .github/workflows/playwright.yml: pipeline de integração contínua do GitHub Actions.
Pré-requisitos
- Python 3.13 (recomendado, mesma versão configurada no workflow).
- Git.
- Navegador Chromium instalado pelo Playwright.
- Visual Studio Code ou outro editor de sua preferência.
Como executar o projeto localmente
1. Clone o repositório
git clone URL_DO_SEU_REPOSITORIO
cd Projeto-2
Substitua URL_DO_SEU_REPOSITORIO pelo endereço HTTPS do seu repositório no GitHub.
2. Crie e ative o ambiente virtual
Windows — PowerShell:
python -m venv venv
.\venv\Scripts\Activate.ps1
Se o PowerShell bloquear a ativação, consulte a política de execução do seu ambiente ou ative o ambiente pelo terminal do VS Code.
3. Instale as dependências
python -m pip install --upgrade pip
pip install -r requirements.txt
4. Instale os navegadores do Playwright
Para instalar o Chromium:
python -m playwright install chromium
5. Execute todos os testes
pytest
Para acompanhar a execução abrindo o navegador e desacelerando as ações:
pytest --headed --slowmo 1000
Para executar somente um arquivo:
pytest tests/test_001_login.py
pytest tests/test_002_pix_realizado.py
Para executar um teste específico pelo nome:
pytest -k test_002_pix_realizado
Integração contínua — GitHub Actions
O arquivo .github/workflows/playwright.yml configura a execução dos testes no GitHub Actions.

O workflow é acionado em eventos de push e pull request direcionados à branch main. Ele prepara o ambiente Python, instala as dependências, instala os navegadores do Playwright e executa o Pytest.

Em caso de falha, o workflow está configurado para tentar disponibilizar o artefato de traces do Playwright, quando gerado.

Para acompanhar:
1. Abra o repositório no GitHub.
2. Acesse a aba Actions.
3. Selecione o workflow Playwright Tests.
4. Abra uma execução para consultar os logs e o resultado.
Resultado da execução local
Na última execução compartilhada, os dois testes passaram:
tests/test_001_login.py          . [ 50%]
tests/test_002_pix_realizado.py  . [100%]

2 passed
Esse resultado registra a execução realizada naquele momento; novas execuções podem apresentar resultados diferentes conforme o estado e a disponibilidade do ambiente de demonstração.
Próximas melhorias
- Ampliar a cobertura com cenários negativos de Pix (chave inválida, valor vazio e valor inválido).
- Adicionar evidências de execução e relatórios ao repositório.
- Melhorar a validação de mensagens e dados apresentados na aplicação.
- Avaliar a geração e publicação de relatórios HTML no pipeline CI.
Projeto de estudo de QA Automation, desenvolvido para praticar automação de testes web com Python, Playwright, Pytest e Page Object Model.
