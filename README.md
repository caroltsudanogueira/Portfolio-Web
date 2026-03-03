# Portfólio de Engenharia Biomédica - Carolina

Este projeto é um portfólio profissional desenvolvido para apresentar projetos e competências na área de Engenharia Biomédica. A aplicação foi construída utilizando Django e está totalmente integrada a um banco de dados em nuvem.

## URL Pública Ativa
O projeto está em produção e pode ser acessado através do link abaixo:
👉 **[Acesse o meu Portfólio aqui](https://portfolio-carolina-t-n.onrender.com/)** 

---

## Tecnologias Utilizadas

* **Linguagem:** Python 3.12
* **Framework Web:** Django 6.0.2
* **Banco de Dados:** PostgreSQL (Hospedado via **Neon.tech**)
* **Estilização:** Tailwind CSS
* **Servidor de Produção:** Gunicorn & Whitenoise
* **Deploy:** Render

---

## Arquitetura de Dados Implementada

A aplicação segue uma arquitetura baseada em nuvem para garantir segurança e escalabilidade dos dados:

```text
[ Usuário/Browser ] 
       ↕ (HTTPS)
[ Render (PaaS) ] <--- Servidor Python com Gunicorn
       ↕ (ORM Django)
[ Neon (DBaaS) ] <--- Banco de Dados PostgreSQL Gerenciado
Frontend: Interface responsiva que consome dados dinâmicos do backend.
Backend: Lógica em Django que gerencia os modelos de projetos e o formulário de contato.
Persistência: Dados armazenados de forma segura no Neon, utilizando variáveis de ambiente para proteção de credenciais.

##Documentação de Rotas (API Interna)
RotaMétodoDescrição/GETHome: Exibe a bio, habilidades e a galeria de projetos técnicos.
/admin/GET/POSTPainel Administrativo: Interface para gestão de conteúdos e mensagens.
/contato/POSTEndpoint de Contato: Processa e armazena mensagens no banco de dados.

##Guia de Execução Local
Se desejar rodar este projeto localmente, siga os passos abaixo:
Clonar o repositório:Bashgit clone [https://github.com/seu-usuario/portfolio.git](https://github.com/seu-usuario/portfolio.git)
cd portfolio
Configurar o ambiente virtual:Bashpython -m venv venv
# No Windows:
.\venv\Scripts\activate
Instalar dependências:Bashpip install -r requirements.txt
Configurar Variáveis de Ambiente:
Crie um arquivo .env na raiz e adicione sua DATABASE_URL do Neon e a SECRET_KEY.
Executar Migrações e Rodar:Bashpython manage.py migrate
python manage.py runserver

O portfólio estará disponível no endereço: http://127.0.0.1:8000/


