pipeline {
    agent any

    stages {
     stage('Install Requirements') {
            steps {
                bat 'pip install -r requirements.txt'
            }

        stage('Run Games') {
            steps {
                bat 'python main.py'
                
            }

            stage('Run Score Page') {
            steps {
                bat 'python main_score.py'
                
            }
        }
    }
}
