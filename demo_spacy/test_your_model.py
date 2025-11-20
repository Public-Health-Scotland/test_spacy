import spacy

nlp = spacy.load("dose_spacy_custom/model-best")  # use the best trained weights
doc = nlp("The patient was prescribed 100mg of ibuprofen for pain relief and 500mg of amoxicillin for the infection.")
for ent in doc.ents:
    print(ent.text, ent.label_)