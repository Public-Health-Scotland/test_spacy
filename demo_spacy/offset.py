import spacy
from spacy.training import Example, offsets_to_biluo_tags

# Load your spaCy model
nlp = spacy.blank("en")  # or spacy.load("en_core_web_sm")

# Your training data
text = "Apple is looking at buying U.K. startup for $1 billion"
entities = [(0, 5, "ORG"), (27, 30, "GPE"), (44, 54, "MONEY")]  # example offsets

# Create a Doc object
doc = nlp.make_doc(text)

# Check if the offsets align with tokens
tags = offsets_to_biluo_tags(doc, entities)
print(tags)  # This will show 'O', 'B-ORG', 'I-ORG', etc., or '-' for misaligned
# If you see '-' in the tags, it means some offsets are misaligned
# You need to adjust the entity spans to match token boundaries
