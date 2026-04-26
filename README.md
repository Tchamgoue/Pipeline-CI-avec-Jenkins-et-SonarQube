# Pipeline CI avec Jenkins et SonarQube pour Application Django Todo

Ce projet démontre une implémentation complète d'un pipeline d'intégration continue (CI) utilisant Jenkins et SonarQube pour analyser la qualité du code d'une application Django simple de gestion de tâches (todo-app).

## Fonctionnalités

- **Application Django** : Application web simple pour gérer des tâches (todo list)
- **Pipeline Jenkins** : Automatisation des tests, analyse de code et déploiement
- **Analyse SonarQube** : Contrôle qualité du code, couverture de tests, sécurité
- **Docker** : Conteneurisation complète des services (Jenkins, SonarQube, application)
- **Tests unitaires** : Tests Django pour valider la logique métier

## Architecture

Le projet utilise Docker Compose pour orchestrer trois services principaux :
- **Jenkins** : Serveur d'automatisation CI/CD (port 8080)
- **SonarQube** : Plateforme d'analyse de qualité du code (port 9000)
- **Todo App** : Application Django de démonstration

## Prérequis

- Docker et Docker Compose installés
- Git pour le versioning
- Navigateur web pour accéder aux interfaces

## Installation

1. **Cloner le repository** :
   ```bash
   git clone <url-du-repo>
   cd Pipeline-CI-avec-Jenkins-et-SonarQube
   ```

2. **Lancer les services** :
   ```bash
   docker compose up -d
   ```

3. **Vérifier que les conteneurs sont démarrés** :
   ```bash
   docker ps
   ```

## Configuration

### Jenkins
- Accédez à http://localhost:8080
- Récupérez le mot de passe initial :
  ```bash
  docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
  ```
- Installez les plugins recommandés lors de la première connexion
- Configurez SonarQube Scanner dans les outils globaux

### SonarQube
- Accédez à http://localhost:9000
- Identifiants par défaut : admin/admin
- Créez un token d'authentification pour Jenkins

### Application Django
L'application est dans le dossier `todo-app/` :
- Modèle Task avec titre, statut (fait/non fait), date de création
- Tests unitaires pour valider les fonctionnalités
- Interface d'administration Django

## Utilisation

### Tests locaux
```bash
cd todo-app
python manage.py test
```

### Pipeline Jenkins
1. Créez un nouveau job pipeline dans Jenkins
2. Pointez vers le Jenkinsfile dans le repository
3. Lancez le build

Le pipeline exécute automatiquement :
- Installation des dépendances Python
- Exécution des tests unitaires
- Analyse SonarQube
- Vérification des critères qualité (Quality Gate)

### Analyse SonarQube
- Visualisez les métriques de qualité du code
- Consultez la couverture de tests
- Identifiez les vulnérabilités et code smells
- Suivez l'évolution de la dette technique

## Structure du projet

```
Pipeline-CI-avec-Jenkins-et-SonarQube/
├── docker-compose.yml          # Configuration Docker Compose
├── Dockerfile.jenkins          # Image Docker personnalisée pour Jenkins
├── Jenkinsfile                 # Pipeline Jenkins
├── sonar-project.properties    # Configuration SonarQube
├── .gitignore                  # Fichiers à ignorer par Git
└── todo-app/                   # Application Django
    ├── config/                 # Configuration Django
    ├── tasks/                  # Application Django des tâches
    ├── manage.py               # Script de gestion Django
    ├── requirements.txt        # Dépendances Python
    ├── db.sqlite3              # Base de données SQLite
    └── sonar-project.properties # Config SonarQube (optionnel)
```

## Technologies utilisées

- **Django** : Framework web Python
- **Jenkins** : Automatisation CI/CD
- **SonarQube** : Analyse qualité du code
- **Docker** : Conteneurisation
- **Python** : Langage de programmation
- **SQLite** : Base de données

## Développement

### Ajouter des tests
Modifiez `todo-app/tasks/tests.py` pour ajouter de nouveaux tests.

### Personnaliser le pipeline
Éditez le `Jenkinsfile` pour ajouter des étapes (déploiement, notifications, etc.).

### Configuration SonarQube
Ajustez `sonar-project.properties` pour personnaliser l'analyse :
- Exclure des fichiers
- Configurer des règles de qualité
- Définir des seuils de couverture

## Dépannage

### Problèmes courants
- **Jenkins ne démarre pas** : Vérifiez les ports 8080 et 50000
- **SonarQube lent** : Augmentez la RAM allouée dans docker-compose.yml
- **Tests échouent** : Activez l'environnement virtuel et installez les dépendances

### Logs utiles
```bash
# Logs Jenkins
docker logs jenkins

# Logs SonarQube
docker logs sonarqube

# Tests Django
cd todo-app && python manage.py test --verbosity=2
```

## Contribution

1. Fork le projet
2. Créez une branche feature (`git checkout -b feature/AmazingFeature`)
3. Committez vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Pushez vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrez une Pull Request

## Licence

Ce projet est réalisé à titre personnel par Adrienne. 