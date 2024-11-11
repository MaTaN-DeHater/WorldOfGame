pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'matanx/wog:latest'
        CONTAINER_NAME = 'wog_container'
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
                    def result = bat(script: "docker-compose exec ${CONTAINER_NAME} python -c 'from WorldOfGame.tests.e2e import test_scores_service; exit(0) if test_scores_service(\"http://localhost:5000\") else exit(1)'", returnStatus: true)
                    if (result != 0) {
                        error('Scores Service test failed')
                    }
                }
            }
        }

        stage('Test: Wipe Scores Button') {
            steps {
                script {
                    def result = bat(script: "docker-compose exec ${CONTAINER_NAME} python -c 'from WorldOfGame.tests.e2e import test_wipe_scores_button; exit(0) if test_wipe_scores_button(\"http://localhost:5000\") else exit(1)'", returnStatus: true)
                    if (result != 0) {
                        error('Wipe Scores Button test failed')
                    }
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', 
                                                      usernameVariable: 'DOCKER_HUB_USERNAME', 
                                                      passwordVariable: 'DOCKER_HUB_PASSWORD')]) {
                        bat '''
                            echo %DOCKER_HUB_PASSWORD% | docker login -u %DOCKER_HUB_USERNAME% --password-stdin
                            docker-compose -f ${DOCKER_COMPOSE_FILE} push
                        '''
                    }
                }
            }
        }

        stage('Finalize') {
            steps {
                script {
                    bat "docker-compose -f ${DOCKER_COMPOSE_FILE} down || true"
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
