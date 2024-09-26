# Grade Curso de TADS

## Instalação e Execução do projeto:

1. Crie um ambiente virtual:
    ```bash
    python -m venv venv
    ```

2. Ative o ambiente virtual:
    
    - No caso de ambiente Windows:
    ```bash
    venv\Scripts\activate
    ```
    
    - No caso de ambiente Linux ou MacOS:
    ```bash
    source venv/bin/activate
    ```

3. Instale o Django:
    ```bash
    pip install django
    ```

4. Rode as migrações:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Rode o servidor:
    ```bash
    python manage.py runserver
    ```
