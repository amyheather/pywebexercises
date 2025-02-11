# pywebexercises

![Python](https://img.shields.io/badge/-python-black?style=for-the-badge&logoColor=white&logo=python&color=3776AB)
![Quarto](https://img.shields.io/badge/-Quarto-black?style=for-the-badge&logoColor=white&logo=quarto&color=0A0A0A)
![Licence](https://licensebuttons.net/l/by-sa/4.0/88x31.png)

Python adaptation of the R webexercises package.

This repository is based on [webexercises](https://github.com/PsyTeachR/webexercises) by Dale Barr and Lisa DeBruine:

> Barr D, DeBruine L (2023). webexercises: Create Interactive Web Exercises in 'R Markdown' (Formerly 'webex'). R package version 1.1.0.9000, https://github.com/psyteachr/webexercises.

It has been adapted so that webexercises can be created using Python. These modifications have been made by [Amy Heather](https://github.com/amyheather) [![ORCID ID](assets/orcid.png)](https://orcid.org/0000-0002-6596-3479).

The modified work is also licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

## 🛠️ Set up

The environment used is provided in an `environment.yaml` file which can be installed as a `conda` environment:

```
conda env create --file environment.yaml
conda activate
```

The provided `environment.yaml` file is a snapshot of the environment used when creating the repository, including **specific package versions**. You can **downgrade or update these packages** if necessary, but be sure to test that everything continues to work as expected after any updates.

As an alternative, a `requirements.txt` file is provided which can be used to set up the environment with `virtualenv`. This is used by GitHub actions, which run much faster with a virtual environment than a conda environment.

## 🔎 Linting

To lint all `.py` and `.ipynb` files, run:

```
bash lint.sh
```