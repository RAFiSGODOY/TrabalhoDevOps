import pytest
from app import app, db, Aluno

# Configuração do teste para o Flask
@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root_password@mariadb/school_db'  # Banco de dados em memória para testes
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Cria as tabelas no banco de dados em memória
        yield client
        with app.app_context():
            db.drop_all()  # Limpa as tabelas após os testes

# Teste para verificar o cadastro de um aluno
def test_cadastro_aluno(client):
    # Dados do novo aluno para enviar na requisição POST
    novo_aluno = {
        "nome": "João",
        "sobrenome": "Silva",
        "turma": "1A",
        "disciplinas": "Matemática, Física"
    }

    # Realiza o POST para cadastrar o aluno
    response = client.post('/alunos', json=novo_aluno)

    # Verifica se o status code é 201 (Criado)
    assert response.status_code == 201

    # Verifica se a resposta contém a mensagem esperada
    assert response.json == {'message': 'Aluno adicionado com sucesso!'}

    # Verifica se o aluno foi realmente adicionado ao banco de dados
    aluno = Aluno.query.filter_by(nome='João').first()
    assert aluno is not None  # Certifica-se de que o aluno foi inserido
    assert aluno.sobrenome == 'Silva'
    assert aluno.turma == '1A'
    assert aluno.disciplinas == 'Matemática, Física'
