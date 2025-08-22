# Contributing

Thank you for your interest in contributing! 🤗

This file covers:

* 🐞 Workflow for bug reports, feature requests and documentation improvements
* 🚀 Workflow for code contributions (bug fixes, enhancements)
* 🛠️ Development
* 📦 Updating the package

<br>

## 🐞 Workflow for bug reports, feature requests and documentation improvements

Before opening an issue, please search [existing issues](https://github.com/amyheather/pywebexercises/issues/) to avoid duplicates. If an issue exists, you can add a comment with additional details and/or upvote (👍) the issue. If there is not an existing issue, please open one and provide as much detail as possible.

* **For feature requests or documentation improvements**, please describe your suggestion clearly.
* **For bugs**, include:
    * Steps to reproduce.
    * Expected and actual behaviour.
    * Environment details (operating system, python version, dependencies).
    * Relevant files (e.g. problematic `.qmd` files).

### Handling bug reports (for maintainers):

* Confirm reproducibility by following the reported steps.
* Label the issue appropriately (e.g. `bug`).
* Request additional information if necessary.
* Link related issues or pull requests.
* Once resolved, close the issue with a brief summary of the fix.

<br>

## 🚀 Workflow for code contributions (bug fixes, enhancements)

1. Fork the repository and clone your fork.

2. Create a new branch for your feature or fix:

```{.bash}
git checkout -b my-feature
```

3. Make your changes and commit them with clear, descriptive messages using the [conventional commits standard](https://www.conventionalcommits.org/en/v1.0.0/).

4. Push your branch to your fork:

```{.bash}
git push origin my-feature
```

5. Open a pull request against the main branch. Describe your changes and reference any related issues.

<br>

## 🛠️ Development

### Dependencies

```
pip install -r requirements.txt
```

### Documentation

```
quarto render
```

### Linting

```
bash lint.sh
```

## 📦 Updating the package

If you are a maintainer and need to publish a new release:

1. Update the `CHANGELOG.md`.

2. Update the version number in `__init__.py`, `CITATION.cff` and `README.md` citation, and update the date in `CITATION.cff`.

3. Create a release on GitHub, which will automatically archive to Zenodo.

4. Build and publish using flit or twine.

To upload to PyPI using `flit`:

```{.bash}
flit publish
```

To upload to PyPI using `twine`: remove any existing builds, then build the package locally and push with twine, entering the API token when prompted:

```{.bash}
rm -rf dist/
flit build
twine upload --repository pypi dist/*
```

For test runs, you can use the same method with test PyPI:

```{.bash}
rm -rf dist/
flit build
twine upload --repository testpypi dist/*
```