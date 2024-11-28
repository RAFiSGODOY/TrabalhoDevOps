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
                    // Verifica se o Python e o pip estão instalados
                    sh '''
                        if ! command -v python3 &> /dev/null
                        then
                            echo "Python3 não encontrado, instalando..."
                            exit 1
                        fi
                        if ! command -v pip &> /dev/null
                        then
                            echo "pip não encontrado, instalando..."
                            curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
                            python3 get-pip.py --user
                        fi

                        # Criar ambiente virtual
                        python3 -m venv venv
                        source venv/bin/activate

                        # Instalar dependências
                        pip install -r requirements.txt
                    '''
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
