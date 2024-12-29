pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/yassinemami13/mini_projet.git'
            }
        }
        stage('Build') {
            steps {
                sh 'echo "Construire le projet"'
            }
        }
        stage('Test') {
            steps {
                sh 'echo "Exécuter les tests"'
            }
        }
        stage('Deploy') {
            steps {
                sh 'echo "Déployer le projet"'
            }
        }
    }
}

