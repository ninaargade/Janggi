pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/ninaargade/Janggi.git']])
            }
        }
        stage('Build') {
            steps {
                git branch: 'main', url: 'https://github.com/ninaargade/Janggi.git'
                sh 'python3 Janggi.py'
            }
        }
        stage('Test') {
            steps {
                sh 'python3 -m unittest unitTests.py'
            }
        }
    }
}
