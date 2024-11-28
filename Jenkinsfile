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
            script {
                // Verificar se Python3 está instalado
                def pythonCheck = sh(script: 'command -v python3 || echo "not found"', returnStdout: true).trim()

                if (pythonCheck == 'not found') {
                    echo "Python3 não encontrado, mas já está instalado no caminho correto: /usr/bin/python3"
                    // Optional: aqui você pode configurar outras dependências ou como o Python deve ser usado
                } else {
                    echo "Python3 está instalado corretamente."
                }

                // Criação do ambiente virtual e instalação das dependências
                sh '''
                    python3 -m venv venv
                    source venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }
    }
}


        stage('Rodar Testes') {
            steps {
                echo 'Executando testes...'
                dir('flask') {
                    sh '''
                        source venv/bin/activate
                        pytest --junitxml=pytest.xml
                    '''
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
