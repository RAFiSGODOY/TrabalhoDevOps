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
                    // Verifica se o Python e o pip estão instalados e instala o pip caso necessário
                    sh '''
                        if ! command -v python3 &> /dev/null
                        then
                            echo "Python3 não encontrado, instalando..."
                            apt-get install python3
                        fi
                        if ! command -v pip &> /dev/null
                        then
                            echo "pip não encontrado, instalando..."
                            curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
                            python3 get-pip.py --user
                        fi

                        # Criar um ambiente virtual
                        python3 -m venv venv

                        # Ativar o ambiente virtual
                        source venv/bin/activate

                        # Instalar as dependências dentro do ambiente virtual
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
                        # Ativar o ambiente virtual
                        source venv/bin/activate

                        # Rodar os testes
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
