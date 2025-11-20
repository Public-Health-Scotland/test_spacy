from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline
import pandas as pd

# local folder where the model will be downloaded the very first time
model_dir = '.model/'

models = ["dslim/bert-base-NER", "dslim/bert-large-NER", "dslim/distilbert-NER"]
option_selected = 1
print("selecteed", models[option_selected])

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(models[option_selected], cache_dir=model_dir)
model = AutoModelForTokenClassification.from_pretrained(models[option_selected], cache_dir=model_dir)

# Create a NER pipeline
ner_pipeline = pipeline("ner", model=model, tokenizer=tokenizer)

# Example text
text = """The patient is diagnosed with Alzheimer's disease. 
She is Vitamin D deficient.The patient is 35 years old. The age of the patient is 35 years.
The patient was prescribed 500mg of Amoxicillin. Patient should take 5 mg of Prednisone daily.
"""

# Perform NER
ner_results = ner_pipeline(text)

# for entity in ner_results:
#     print(f"Entity: {entity['word']}, Label: {entity['entity']}")

df = pd.DataFrame(ner_results)
print(df)
