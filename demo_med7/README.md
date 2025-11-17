# med7 NER
- Create a Python 3.11 venv: `/opt/python/3.11.13/bin/python3 -m venv demo_med7/.venvmed7`
- Activate this venv: `source demo_med7/.venvmed7/bin/activate`
- Update your venv pip: `pip install --upgrade pip`
- Install wheel package to speed up package installation: `pip install wheel`
- install packages from requirements.txt which is part of this subfolder: `pip install -r demo_med7/requirements.txt --prefer-binary`
- Install med7 (Last updated Nov 19, 2022): `pip install https://huggingface.co/kormilitzin/en_core_med7_lg/resolve/refs%2Fpr%2F3/en_core_med7_lg-3.4.2.1-py3-none-any.whl`
- Run test_med7.py script using this command: `python test_med7.py`
. You will find more info here: https://github.com/kormilitzin/med7
- Article about med7: https://kormilitzin.medium.com/med7-clinical-information-extraction-system-in-python-and-spacy-5e6f68ab1c68

## Considerations
- Med 7 works only with numpy 1.26.4 and spacy 3.4.4. They are not compatible with Python 3.12


## Diagram

![Diagram](ed7.drawio.svg)