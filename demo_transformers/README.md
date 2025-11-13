# transformers NER
- Create a Python 3.13 venv: `python -m venv demo_transformers/.venvtrans`
- Activate this venv: `source demo_transformers/.venvtrans/bin/activate`
- Update your venv pip: `pip install --upgrade pip`
- Install wheel package to speed up package installation: `pip install wheel`
- Install packages from requirements.txt which is part of this subfolder: `pip install -r demo_transformers/requirements.txt --prefer-binary`
- Run biomed example: `python test_biomed.py`

# Transformers
These models can work with sentiment analysis, named entity recognition, question answering, and text classification:

- Bert
- DistilBert
- RoBerta
- ModernBert

There is a customised model for medical purposes:

[Biomed](https://huggingface.co/d4data/biomedical-ner-all)

