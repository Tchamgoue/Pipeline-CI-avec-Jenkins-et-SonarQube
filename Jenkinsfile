pipeline {
    agent any

    environment {
        SONAR_SCANNER_HOME = tool 'SonarQube Scanner'
        APP_DIR = 'todo-app'
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Code récupéré depuis GitHub'
            }
        }

        stage('Install Dependencies') {
            steps {
                dir("${APP_DIR}") {
                    sh '''
                        python3 -m venv venv
                        . venv/bin/activate
                        pip install -r requirements.txt
                        pip install coverage
                    '''
                }
            }
        }

        stage('Run Tests') {
            steps {
                dir("${APP_DIR}") {
                    sh '''
                        . venv/bin/activate
                        coverage run manage.py test
                        coverage xml -o coverage.xml
                    '''
                }
            }
            post {
                always {
                    echo 'Tests terminés'
                }
                failure {
                    echo '❌ Des tests ont échoué !'
                }
            }
        }

        stage('SonarQube Analysis') {
            steps {
                dir("${APP_DIR}") {
                    withSonarQubeEnv('SonarQube-local') {
                        sh "${SONAR_SCANNER_HOME}/bin/sonar-scanner"
                    }
                }
            }
        }

        stage('Quality Gate') {
            steps {
                timeout(time: 2, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline terminé avec succès !'
        }
        failure {
            echo '❌ Le pipeline a échoué.'
        }
    }
}
