#!/bin/bash

echo "🎨 Formatage du code avec Black et isort..."

# Formatage avec isort (imports)
echo "📦 Organisation des imports avec isort..."
isort . --profile=black --skip-glob="*/migrations/*" --skip-glob="*/__pycache__/*" --skip-glob="*/env/*" --skip-glob="*/.pytest_cache/*"

# Formatage avec Black
echo "⚫ Formatage du code avec Black..."
black . --exclude="/(migrations|__pycache__|env|\.pytest_cache)/" --line-length=88 --include="\.py$"

echo "✅ Formatage terminé ! Votre code respecte maintenant les normes PEP8."
