import spacy
from spacy.training.example import Example
import pandas as pd
import ast

# Custon data
data = pd.read_csv('./data/resolved_data_22-Aug-2023-1030.dat', delimiter='|', header=None,
                   names=["classes", "sentence", "indexes"])
def safe_eval_list(x: str) -> list:
    if not isinstance(x, str):
        return x
    try:
        return ast.literal_eval(x.strip())
    except (SyntaxError, ValueError):
        fixed = x.strip()
        print(f"error: {fixed}")
        if len(fixed) > 3:
            if not fixed.startswith('[['):
                fixed = '[' + fixed
            if not fixed.endswith(']]'):
                fixed = fixed + ']'
        try:
            return ast.literal_eval(fixed)
        except Exception:
            return None


# fixing dataframe
for col in ['sentence', 'classes', 'indexes']:
    if col == "classes":
        data[col] = data[col].apply(safe_eval_list)
    elif col == "indexes":
        data[col] = data[col].apply(lambda x: ast.literal_eval(x.strip()) if isinstance(x, str) else x)
        data[col] = data[col].apply(
            lambda x: {'entities': [tuple(entity) for entity in x['entities'] if isinstance(entity, list)]} if isinstance(x, dict) else x)
    else:
        data[col] = data[col].apply(lambda x: x.strip() if isinstance(x, str) else x)

print(f"data: {data.shape}")

entities = [item[1] for sublist in data['classes'] for item in sublist]
unique_values = list(set(entities))

TRAIN_DATA = list(zip(data['sentence'], data['indexes']))

# Load blank model
nlp = spacy.blank("en")

# Add NER pipeline
ner = nlp.add_pipe("ner")

# Add labels
for uniq in unique_values:
    ner.add_label("uniq")

# Training loop
optimizer = nlp.begin_training()
for i in range(20):
    for text, annotations in TRAIN_DATA:
        example = Example.from_dict(nlp.make_doc(text), annotations)
        nlp.update([example], sgd=optimizer)

# Save the model
nlp.to_disk("./ner_dose_model")
print("task completed!")