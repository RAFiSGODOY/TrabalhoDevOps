pipeline {
    agent any

    environment {
        REPOSITORY_URL = 'https://github.com/RAFiSGODOY/TrabalhoDevOps.git'
        BRANCH_NAME = 'main'
    }

    stages {
        stage('Verificar Docker e Docker Compose') {
            steps {
                script {
                    // Verificar se o Docker está instalado
                    sh 'docker --version'
                    
                    // Verificar se o Docker Compose está instalado
                    sh 'docker-compose --version'
                }
            }
        }

        stage('Baixar código do Git') {
            steps {
                // Clonar o repositório do Git
                git branch: "${BRANCH_NAME}", url: "${REPOSITORY_URL}"
            }
        }

        stage('Build e Deploy') {
            steps {
                script {
                    // Construir as imagens Docker e subir os containers
                    sh 'docker-compose up --build -d'
                }
            }
        }

        stage('Rodar Testes') {
            steps {
                script {
                    // Rodar os testes com o pytest (ou qualquer outra ferramenta de testes que você esteja utilizando)
                    sh 'sleep 40' // Esperar o ambiente subir completamente
                    sh 'docker-compose run --rm test' // Subir o container de teste e executar
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline executada com sucesso!'
        }
        failure {
            echo 'A pipeline falhou.'
        }
    }
}
