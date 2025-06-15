pipeline {
    agent any

    environment {
        VENV_DIR = "venv"
    }

    stages {
        stage('Checkout') {
            steps {
                // Clone ton repo
                checkout scm
            }
        }

        stage('Setup Python') {
            steps {
                sh 'python3 -m venv $VENV_DIR'
                sh './$VENV_DIR/bin/pip install --upgrade pip'
                sh './$VENV_DIR/bin/pip install selenium pytest webdriver-manager'
            }
        }

        stage('Run Tests') {
            steps {
                // Lance les tests
                sh './$VENV_DIR/bin/pytest --headless'
            }
        }
    }

    post {
        always {
            // Affiche les fichiers de log ou captures d'écran si tu les génères
            archiveArtifacts artifacts: '**/*.png', allowEmptyArchive: true
            junit '**/test-results.xml'  // si tu ajoutes l'option de sortie XML à pytest
        }
    }
}

