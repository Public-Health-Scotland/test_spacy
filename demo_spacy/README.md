# spacy NER
- Create a Python 3.13 venv: python -m venv demo_spacy/.venvspac
- Activate this venv: source demo_spacy/.venvspac
- install packages from requirements.txt which is part of this folder
- Run download_models.py to download some models or you can install a model with this command: python -m spacy download en_core_web_sm
- Run test_demo_spacy.py
- You will be able to see some values in terminal related to amounts. (e.g. 100mg 500mg)

## Train your model
- If you train spacy with your own data you can create your own package using: python -m spacy package ./ner_dose_model ./dose_ner --name dose_ner_test --version 1.0.0
- These packages are important to create your executable whl: `pip install build twine`
- Navigate to the directory where your model package is (e.g., ./output/en_my_model-1.0.0) and run: `python -m build`
- Use twine to upload your package: `twine upload dist/*`
