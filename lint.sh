#!/bin/bash

echo "Linting package..."
pylint ./pywebexercises

echo "Linting quarto pages..."
for qmd_file in pages/*.qmd; do
    base_name=$(basename "$qmd_file" .qmd)
    quarto render "$qmd_file" --to ipynb
    nbqa pylint "_site/pages/${base_name}.ipynb"
    rm "_site/pages/${base_name}.ipynb"
done

echo "Linting complete."