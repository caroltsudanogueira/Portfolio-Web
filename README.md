# Portfolio-Web
 Portfólio de Engenharia Biomédica - Carolina Tsuda Nogueira
Este projeto é um portfólio dinâmico desenvolvido com Django e Tailwind CSS, utilizando o banco de dados Neon (PostgreSQL). 

Tecnologias Utilizadas
  Back-end: Python 3.12 / Django 6.0.2
  
  Banco de Dados: PostgreSQL (Hospedado no Neon)
  
  Front-end: HTML5, CSS3 e Tailwind CSS
  
  Gestão de Dependências: python-dotenv e dj-database-url para segurança de credenciais.

Como Iniciar o Projeto Localmente
Siga os passos abaixo para configurar o ambiente e rodar o servidor na sua máquina:

1. Clonar o Repositório
  Bash
  git clone https://github.com/caroltsudanogueira/Portfolio-Web
  cd portfolio

3. Criar e Ativar o Ambiente Virtual (Venv)
  Bash
  # No Windows
  python -m venv venv
  venv\Scripts\activate

3. Instalar as Dependências
  Bash
  pip install django dj-database-url python-dotenv pillow

4. Configurar as Variáveis de Ambiente
  Crie um arquivo chamado .env na raiz do projeto e adicione as suas credenciais do banco de dados Neon e a sua Secret Key do Django:

Snippet de código
  DATABASE_URL=seu_link_do_neon_aqui
  SECRET_KEY=sua_chave_secreta_aqui
  DEBUG=True
  
5. Sincronizar o Banco de Dados
  Para criar as tabelas de Projetos, Categorias e Contatos no banco de dados, execute:
    Bash
    python manage.py makemigrations
    python manage.py migrate
    
6. Iniciar o Servidor
  Bash
  python manage.py runserver

O portfólio estará disponível no endereço: http://127.0.0.1:8000/
