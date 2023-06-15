#!/bin/bash

# Directory structure
DIRS=(
"app/main"
"app/transactions"
"app/users"
"app/templates/main"
"app/templates/transactions"
"app/templates/users"
"app/static"
)

# Python files
PYFILES=(
"app/main/__init__.py"
"app/transactions/__init__.py"
"app/users/__init__.py"
"app/main/routes.py"
"app/transactions/routes.py"
"app/users/routes.py"
"app/main/forms.py"
"app/transactions/forms.py"
"app/users/forms.py"
"app/models.py"
"app/email.py"
"app/__init__.py"
"tests.py"
"config.py"
)

# Env and requirements
TOUCHFILES=(
"requirements.txt"
)

echo "Creating directories..."
for dir in "${DIRS[@]}"; do
  mkdir -p $dir
done

echo "Creating Python files..."
for file in "${PYFILES[@]}"; do
  touch $file
done

echo "Creating environment files..."
for file in "${TOUCHFILES[@]}"; do
  touch $file
done

echo "Finished creating Flask project structure."
