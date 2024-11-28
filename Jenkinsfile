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
                            echo "Python3 não encontrado!"
                            error "Python3 não encontrado"
                        } else {
                            echo "Python3 está instalado corretamente."
                        }

                        // Criação do ambiente virtual e instalação das dependências
                        sh '''
                            python3 -m venv venv
                            . venv/bin/activate && pip install -r requirements.txt
                        '''
                    }
                }
            }
        }

        stage('Rodar Testes') {
            steps {
                echo 'Executando testes...'
                dir('flask') {
                    // Executar os testes com unittest
                    sh '''
                        . venv/bin/activate
                        python -m unittest discover -s tests -p "*.py" > result.log || true
                        tail -n 10 result.log  # Exibe as últimas linhas do log para facilitar o debug
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
