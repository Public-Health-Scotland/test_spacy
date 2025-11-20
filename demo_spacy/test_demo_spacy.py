import spacy
import pandas as pd


models = ["en_core_web_lg", "en_core_web_sm"]

selected_model = models[0]

nlp = spacy.load(selected_model)

print(f"The model is in {nlp._path} folder path")

# Example text data
texts = ["The patient was prescribed 100mg of ibuprofen for pain relief and 500mg of amoxicillin for the infection."]
print(texts)

# Process texts
docs = [nlp(text) for text in texts]

# Extract entities
for doc in docs:
    for ent in doc.ents:
        print(ent.text, ent.label_)
