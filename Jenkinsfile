pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'matanx/wog:latest'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                dir('WorldOfGame') {
                    git url: 'https://github.com/MaTaN-DeHater/WorldOfGame.git'
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    
                    bat "docker build -t ${DOCKER_IMAGE} WorldOfGame"
                }
            }
        }

        stage('Run') {
            steps {
                script {
                    
                    bat "docker run -d -p 5000:5000 -v %WORKSPACE%\\scores.json:/app/scores.json ${DOCKER_IMAGE}"
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    
                    def result = bat(script: 'python WorldOfGame\\tests\\e2e.py', returnStatus: true)
                    if (result != 0) {
                        error('Tests failed')
                    }
                }
            }
        }

        stage('Finalize') {
            steps {
                script {
                    
                    def containerId = bat(script: "docker ps -q --filter ancestor=${DOCKER_IMAGE}", returnStdout: true).trim()
                    if (containerId) {
                        bat "docker stop ${containerId}"
                    }

                    
                    docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials') {
                        bat "docker push ${DOCKER_IMAGE}"
                    }
                }
            }
        }
    }
}
