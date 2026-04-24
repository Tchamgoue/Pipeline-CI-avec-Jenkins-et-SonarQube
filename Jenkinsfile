pipeline {
    agent any   // Utilise n'importe quel agent Jenkins disponible

    environment {
        SONAR_SCANNER_HOME = tool 'SonarQube Scanner'  // Référence l'outil déclaré dans Jenkins
    }

    stages {

        stage('Checkout') {
            // Jenkins clone automatiquement le repo ici
            // Cette étape est souvent implicite mais on la rend visible
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
                    pip install coverage   # Pour mesurer la couverture de tests
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    coverage run manage.py test
                    coverage xml -o coverage.xml   # Génère un rapport XML pour SonarQube
                '''
            }
            post {
                always {
                    // Même en cas d'échec, on publie les résultats de test
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
                    // withSonarQubeEnv injecte automatiquement l'URL et le token
                    sh "${SONAR_SCANNER_HOME}/bin/sonar-scanner"
                }
            }
        }

        stage('Quality Gate') {
            steps {
                timeout(time: 2, unit: 'MINUTES') {
                    // Attend que SonarQube ait fini son analyse
                    // et échoue le pipeline si les seuils de qualité ne sont pas atteints
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
