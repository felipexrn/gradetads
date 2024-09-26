# Grade Curso de TADS

## Instalação e Execução do projeto:

1. **Crie um ambiente virtual:**
    ```bash
    python -m venv venv
    ```

2. **Ative o ambiente virtual:**
    
    - No caso de ambiente Windows:
    ```bash
    venv\Scripts\activate
    ```
    
    - No caso de ambiente Linux ou MacOS:
    ```bash
    source venv/bin/activate
    ```

3. **Instale o Django:**
    ```bash
    pip install django
    ```

4. **Caminhe para o doretório do projeto:**
    ```bash
    cd grade_tads
    ```

5. **Rode as migrações:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. **Rode o servidor:**
    ```bash
    python manage.py runserver
    ```

## Operação do sistema:
1. **Visualizando a grade curricular:**

Abra o navegador acesse a rota `http://127.0.0.1:8000/`. Lá você verá a grade do curso e as disciplinas com suas respectivas cargas horárias. Marque as disciplinas como concluídas ou não concluídas. Veja a soma total de carga horária cumprida.

2. **Adicionando, removendo ou alterando disciplinas:**

Faça login com admin na rota `http://127.0.0.1:8000/login`. Utilize o usuário `admin` e a senha `admin`



