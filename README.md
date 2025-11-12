# **Project**
This Python project contains simple pipelines to create a NER application - November 2025. It also contains subfolders with separate virtual environment creation and their own required packages.

| Subproject/subfolder | Python |
|----------------------|--------|
| demo_spacy           | 3.13.x |
| demo_med7            | 3.11.x |
| demo_transformers    | 3.13.x |
| demo_label           | 3.12.x |

# **spacy**
You need to download one of the available models:
* en_core_web_sm: Small model optimized for CPU, suitable for basic tasks.
* en_core_web_md: Medium model with word vectors, suitable for more complex tasks.
* en_core_web_lg: Large model with extensive word vectors, suitable for high accuracy tasks.
- You can read demo_spacy/README.md to follow some steps

## med7
- If you want to install med7 (Last updated Nov 19, 2022): pip install https://huggingface.co/kormilitzin/en_core_med7_lg/resolve/refs%2Fpr%2F3/en_core_med7_lg-3.4.2.1-py3-none-any.whl
. You will find more info here: https://github.com/kormilitzin/med7
- Article about med7: https://kormilitzin.medium.com/med7-clinical-information-extraction-system-in-python-and-spacy-5e6f68ab1c68

## Considerations
- Spacy 3.8.8 is currently compatible with Python 3.13.x (Nov 2025). Ref: https://github.com/explosion/spaCy/issues/13658
- Med 7 requires numpy 1.26.4 and spacy 3.4.4 and it is not compatible with Python 3.12

# Transformers
These models can work with sentiment analysis, named entity recognition, question answering, and text classification. There are some base models available for future evaluation
- Bert
- DistilBert
- RoBerta

There are some customised models for medical purposes
- Biomed

# Comments
- This project contains subfolders with each README.md
- You only need to create your Python venv once. The same with the installed packages unless you want to update any of them
- Every time you want to run each subproject secion you need to make sure your virtual env is activated


# Extra tools
- https://universe.roboflow.com/fast-nuces-xcmbn/prescription-labeling/dataset/3#
- curl -L "https://universe.roboflow.com/ds/dsYQAnDdyu?key=Hx3NcG9JDD" > roboflow.zip; unzip roboflow.zip; rm roboflow.zip

### Resource

[How to use VS code in Posit Workbench](https://github.com/Public-Health-Scotland/vscode_prep)
[Fine tune models](https://huggingface.co/Simonlee711/Clinical_ModernBERT)
[Label studio tool for data labeling](https://labelstud.io/)
[Models from Google](https://huggingface.co/google-bert)
[Models from Meta](https://huggingface.co/FacebookAI)
