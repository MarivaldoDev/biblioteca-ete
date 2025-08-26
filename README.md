# Biblioteca ETE

# Descrição do Projeto
Esta aplicação foi desenvolvida especialmente para atender às necessidades da biblioteca da minha escola, onde concluí o Ensino Médio. O sistema trouxe melhorias significativas na organização dos cadastros de usuários e livros, facilitando o gerenciamento das informações. Além disso, a funcionalidade de cobrança automática de devoluções atrasadas foi essencial para otimizar o controle dos empréstimos, reduzindo o trabalho manual e garantindo maior eficiência na administração da biblioteca. Com essas soluções, o projeto tornou o dia a dia dos responsáveis e dos usuários muito mais prático e ágil.


# Funcionalidades
- **Cadastro de Usuários**  
  Permite que novos usuários se registrem no sistema, armazenando informações como nome, e-mail e senha. Usuários cadastrados podem acessar todas as funcionalidades do sistema.

- **Empréstimos de Livros**  
  Usuários podem buscar livros disponíveis e realizar empréstimos. O sistema controla quais livros estão emprestados, para quem e por quanto tempo.

- **Sistema de Login / Logout**  
  Garante que apenas usuários autenticados possam acessar funcionalidades restritas, como realizar empréstimos ou visualizar histórico. O login protege os dados dos usuários e o logout encerra a sessão de forma segura.

- **Cobrança automatizada de prazos expirados**  
  O sistema monitora os prazos dos empréstimos e envia notificações automáticas para usuários que não devolveram os livros no prazo, podendo gerar cobranças ou alertas conforme a política definida.



## ⚙️ Como Executar Localmente

1. Clone o repositório:
   ```bash
   git clone https://github.com/MarivaldoDev/biblioteca-ete.git
   cd biblioteca-ete
   ```

2. Crie e ative um ambiente virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate     # Windows
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4. Configure o .env com suas variáveis (Redis, banco de dados e etc.).

5. Aplique as migrações:
    ```bash
    python3 manage.py migrate # Linux/macOS
    python manage.py migrate # Windows
    ```

6. Inicie o servidor:
    ```bash
    python3 manage.py runserver # Linux/macOS
    python manage.py runserver # Windows
    ```


## 🐳 Executando com Docker

1. Certifique-se de ter o Docker e o Docker Compose instalados.

2. Construa e inicie os containers:
    ```bash
    docker-compose up --build
    ```

3. Acesse a aplicação em [http://localhost:8000](http://localhost:8000).

<br>

# Pré - Visualização
![Image](https://github.com/user-attachments/assets/d57a7590-eea4-4eb1-ae1b-330ee4d6ae7d)



# Contato
Autor: Marivaldo Pedro
<br>
E-mail: marivaldo.pedro.dev@outlook.com
