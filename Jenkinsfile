pipeline {
    agent {
        docker {
            image 'python:3.12-slim'
            // Donne accès au socket Docker si besoin (optionnel ici)
            args '--user root'
        }
    }

    environment {
        SONAR_SCANNER_HOME = tool 'SonarQube Scanner'
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Code récupéré depuis GitHub'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                    pip install coverage
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    coverage run manage.py test
                    coverage xml -o coverage.xml
                '''
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
                withSonarQubeEnv('SonarQube-local') {
                    sh "${SONAR_SCANNER_HOME}/bin/sonar-scanner"
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