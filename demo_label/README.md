# Label studio
This label studio tool is compatible with Python 3.12 (Nov 2025) but it is **not working** in Posit Workbench. It needs some additional configuration related to proxy

- Create a Python 3.12 venv: `/opt/python/3.12.12/bin/python3 -m venv demo_label/.venvlabel`
- Activate this venv: `source demo_label/.venvlabel/bin/activate`
- Update your venv pip: `pip install --upgrade pip`
- Install packages from requirements.txt which is part of this subfolder: `pip install -r demo_label/requirements.txt --prefer-binary`
- Run this command to open the tool: `label-studio`
- This command will give you more options: `label-studio --help`
