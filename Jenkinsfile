pipeline{
    agent any
    stages {
        stage("Code Quality/Linting")
        {
            sh'''
            poetry install
            poetry run black . --check --line-length=88
            poetry run isort . --force-single-line-imports", "--line-length", "88", "--profile", "black
            poetry run flake8 --max-line-length 88 --extend-ignore=E501,E203,E503
            poetry run bandit .
            poetry run safety check
            '''
        }
    }
}
