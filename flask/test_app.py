import unittest
import logging
from app import app, db, Aluno  # Ajuste conforme o nome do seu app e modelo

# Configuração do logger
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class TestApp(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        """Configuração inicial antes dos testes."""
        # Configure o banco de dados para os testes
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root_password@mariadb/school_db'
        app.config['TESTING'] = True
        cls.client = app.test_client()  # Cria um cliente para fazer requisições
        db.create_all()  # Cria as tabelas para o teste
        logger.info('Banco de dados configurado para os testes.')
    
    @classmethod
    def tearDownClass(cls):
        """Limpeza após os testes."""
        db.session.remove()
        db.drop_all()  # Remove as tabelas do banco de dados
        logger.info('Banco de dados limpo após os testes.')

    def test_database_connection(self):
        """Teste para verificar se a conexão com o banco de dados funciona e registrar o cadastro do aluno."""
        with app.app_context():
            try:
                # Testando uma operação simples no banco, como adicionar um aluno
                aluno = Aluno(nome="Test Aluno", matricula="12345")
                db.session.add(aluno)
                db.session.commit()
                logger.info(f"Aluno cadastrado: {aluno.nome}, Matrícula: {aluno.matricula}")
                
                # Verifica se o nome foi corretamente inserido
                self.assertEqual(aluno.nome, "Test Aluno")
                self.assertEqual(aluno.matricula, "12345")
                logger.info(f"Cadastro do aluno {aluno.nome} confirmado.")
                
            except Exception as e:
                logger.error(f"Erro ao conectar ao banco de dados ou ao cadastrar aluno: {e}")
                self.fail(f"Erro ao conectar ao banco de dados: {e}")

    def test_home_page(self):
        """Teste simples para a página inicial."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome', response.data)  # Verifique a presença de 'Welcome' na página inicial

if __name__ == '__main__':
    unittest.main()
