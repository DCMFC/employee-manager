
Site Administrador:

    http://127.0.0.1:8000/admin/
    Usuário: admin
    Senha: admin

Collection postman:
    
    Testes.postman_collection.json

APIs

| Verbo         | URI           | Descrição                                       |
| ------------- | ------------- | ------------------------------------------------|
| GET           | /employee/    | Lista todos os "Employees"                      |
| GET           | /employee/{id}| Recupera os dados com base no {id}              |
| POST          | /employee/    | Cria um novo "Employee"                         |
| DELETE        | /employee/{id}| Remove um "Employee" com base no {id}           |
| PUT           | /employee/{id}| Atualiza um "Employee" informando todos os dados|
| PATCH         | /employee/{id}| Atualiza um "Employee" parcialmente             |
| POST          | /api-token/   | Gerar token de acesso                           |

Body Employee:

    {
        "name": "Novo",
        "email": "novo@luizalabs.com",
        "department": "Novo"
    }

Incluir no header:

    Authorization:Token 5d7e793b803ee0bfbab7d90333ec0b663ea1b296


Gerar um novo token informar no body:

    username:admin
    password:admin

Instalação:
    
    git clone https://github.com/DCMFC/employee-manager.git
    cd employee-manager/magazine_luiza/
    pip3 install -r requirements.txt
    python3 manage.py runserver
    
