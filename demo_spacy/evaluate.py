import spacy

# Load the saved model
nlp = spacy.load("./ner_dose_model")

# Test data
test_text = """The patient is diagnosed with Alzheimer's disease. 
She is Vitamin D deficient.The patient is 35 years old. The age of the patient is 35 years.
The patient was prescribed 500mg of Amoxicillin. Patient should take 5 mg of Prednisone daily.
"""
# test_text = "Google is opening a new office in New York"

# Process the text
doc = nlp(test_text)

# Print entities
for ent in doc.ents:
    print(ent.text, ent.label_)
