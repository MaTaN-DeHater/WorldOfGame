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
                    def dockerImage = docker.build(DOCKER_IMAGE, 'WorldOfGame')
                }
            }
        }

        stage('Run') {
            steps {
                script {
                    def container = docker.image(DOCKER_IMAGE).run("-d -p 8777:5000 -v $WORKSPACE/scores.json:/app/scores.json")
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    // Run the tests and check if they pass
                    def result = sh(script: 'python WorldOfGame/tests/e2e.py', returnStatus: true)
                    if (result != 0) {
                        error('Tests failed')
                    }
                }
            }
        }

        stage('Finalize') {
            steps {
                script {
                    
                    def containerId = sh(script: "docker ps -q --filter ancestor=${DOCKER_IMAGE}", returnStdout: true).trim()
                    if (containerId) {
                        sh "docker stop ${containerId}"
                    }
                    
                    
                    docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials') {
                        docker.image(DOCKER_IMAGE).push()
                    }
                }
            }
        }
    }
}
