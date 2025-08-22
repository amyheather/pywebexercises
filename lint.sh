#!/bin/bash

echo "Linting package..."
pylint src

echo "Linting quarto pages..."
lintquarto -l pylint -p docs
