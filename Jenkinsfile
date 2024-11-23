pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Baixa o código do repositório
                checkout scm
            }
        }

        stage('Build') {
            steps {
                // Comandos para construir o projeto
                sh 'echo "Building the project..."'
                sh 'docker-compose up --build -d' 
            }
        }

        stage('Test') {
            steps {
                // Comandos para rodar os testes
                sh 'echo "Running tests..."'
                sh 'make test' // Substitua pelo comando de teste real
            }
        }

        stage('Deploy') {
            steps {
                // Comandos para deploy
                sh 'echo "Deploying the application..."'
                sh './deploy.sh' // Substitua pelo seu script de deploy
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
