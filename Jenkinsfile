pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Preparar Ambiente') {
            steps {
                echo 'Instalando dependências do Python...'
                dir('flask') {
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Rodar Testes') {
            steps {
                echo 'Executando testes...'
                dir('flask') {
                    // Executar os testes com pytest (test_app.py já verifica o cadastro)
                    sh 'pytest --junitxml=pytest.xml'
                }
            }
        }

        stage('Build e Deploy') {
            steps {
                echo 'Construindo e subindo os containers Docker...'
                sh 'docker-compose up --build -d'
            }
        }
    }

    post {
        always {
            echo 'Pipeline finalizado!'
        }
        success {
            echo 'Pipeline concluído com sucesso!'
        }
        failure {
            echo 'Pipeline falhou!'
        }
    }
}
