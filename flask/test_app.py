import unittest
from app import app, db, Aluno  # Ajuste conforme o nome do seu app e modelo

class TestApp(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        """Configuração inicial antes dos testes."""
        # Configure o banco de dados para os testes
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://user:password@localhost:3306/dbname'
        app.config['TESTING'] = True
        cls.client = app.test_client()  # Cria um cliente para fazer requisições
        db.create_all()  # Cria as tabelas para o teste

    @classmethod
    def tearDownClass(cls):
        """Limpeza após os testes."""
        db.session.remove()
        db.drop_all()  # Remove as tabelas do banco de dados
 
    def test_database_connection(self):
        """Teste para verificar se a conexão com o banco de dados funciona."""
        with app.app_context():
            try:
                # Testando uma operação simples no banco, como adicionar um aluno
                aluno = Aluno(nome="Test Aluno", matricula="12345")
                db.session.add(aluno)
                db.session.commit()
                self.assertEqual(aluno.nome, "Test Aluno")  # Verifica se o nome foi corretamente inserido
            except Exception as e:
                self.fail(f"Erro ao conectar ao banco de dados: {e}")

    def test_home_page(self):
        """Teste simples para a página inicial."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome', response.data)  # Verifique a presença de 'Welcome' na página inicial

if __name__ == '__main__':
    unittest.main()
