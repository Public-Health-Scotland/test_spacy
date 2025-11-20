import spacy
from spacy import displacy

# Load model
nlp = spacy.load("en_core_web_lg")

# Process text
doc = nlp("The patient was prescribed 100mg of ibuprofen for pain relief and 500mg of amoxicillin for the infection.")

colors = {"QUANTITY": "linear-gradient(90deg, #aa9cfc, #fc9ce7)"}
options = {"colors": colors}

# Render in Jupyter Notebook
# displacy.render(doc, style="dep", jupyter=True)

# Or serve in a local web server
displacy.serve(doc, style="ent", options=options)
