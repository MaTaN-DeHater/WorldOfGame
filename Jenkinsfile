pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "matanx/wog:latest"
    }

    stages {
        stage('Checkout') {
            steps {
              checkout scm
                dir('WorldOfGame') {
                    git url: 'https://github.com/MaTaN-DeHater/WorldOfGame.git'
            }
        }
        
        stage('Build Docker Image') {
            steps {
               
                script {
                    sh 'docker-compose -f docker-compose.yml build'
                }
            }
        }

        stage('Run Docker Container') {
            steps {
               
                script {
                    sh 'docker-compose -f docker-compose.yml up -d'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    
                    sh 'docker-compose exec wog_service python /app/WorldOfGame/tests/e2e.py'
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', 
                                                      usernameVariable: 'DOCKER_HUB_USERNAME', 
                                                      passwordVariable: 'DOCKER_HUB_PASSWORD')]) {
                        sh '''
                        echo $DOCKER_HUB_PASSWORD | docker login -u $DOCKER_HUB_USERNAME --password-stdin
                        docker tag ${DOCKER_IMAGE} ${DOCKER_HUB_USERNAME}/${DOCKER_IMAGE}
                        docker push ${DOCKER_HUB_USERNAME}/${DOCKER_IMAGE}
                        '''
                    }
                }
            }
        }

        stage('Finalize') {
            steps {
               
                script {
                    sh 'docker-compose -f docker-compose.yml down || true'
                }
            }
        }
    }

    post {
        always {
            
            sh 'docker-compose -f docker-compose.yml down || true'
            cleanWs()
        }
        failure {
            echo 'Build or tests failed. Check the console output for details.'
        }
        success {
            echo 'All stages completed successfully!'
        }
    }
}
