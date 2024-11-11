pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'matanx/wog:latest'
        DOCKER_COMPOSE_FILE = 'docker-compose.yml'
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
                    
                    bat "docker-compose -f ${DOCKER_COMPOSE_FILE} build"
                }
            }
        }

        stage('Run') {
            steps {
                script {
                    
                    bat "docker-compose -f ${DOCKER_COMPOSE_FILE} up -d"
                }
            }
        }

        stage('Test: Scores Service') {
            steps {
                script {
                    def result = bat(script: "docker-compose exec wog_service python /app/WorldOfGame/tests/e2e.py test_scores_service http://localhost:5000", returnStatus: true)
                    if (result != 0) {
                        echo "Scores Service test failed"
                    }
                }
            }
        }

        stage('Test: Wipe Scores Button') {
            steps {
                script {
                    def result = bat(script: "docker-compose exec wog_service python /app/WorldOfGame/tests/e2e.py test_wipe_scores_button http://localhost:5000", returnStatus: true)
                    if (result != 0) {
                        echo "Wipe Scores Button test failed"
                    }
                }
            }
        }

        stage('Finalize') {
            steps {
                script {
                    
                    bat "docker-compose -f ${DOCKER_COMPOSE_FILE} down"
                   
                    docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials') {
                        bat "docker-compose push"
                    }
                }
            }
        }
    }

    post {
        always {
            script {
               
                bat "docker-compose -f ${DOCKER_COMPOSE_FILE} down || true"
            }
        }
    }
}
