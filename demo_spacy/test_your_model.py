from ast import literal_eval
import spacy
import pandas as pd

# Load your test file
df = pd.read_csv("data/test.csv")

# load your trained model
nlp = spacy.load(".model/ner_dose_model/model-best")  # use the best trained weights

true_entities = []
pred_entities = []

for index, row in df.iterrows():
    # get predictions per sentence
    doc = nlp(str(row["sentence"]))
    # format predictions
    pred = [tuple([ent.start_char, ent.end_char, ent.label_]) for ent in doc.ents]
    my_dict = {"entities": pred}
    pred_entities.append(my_dict)

print(f"{len(pred_entities)} sentences were analised and got predicted entitites")

# Convert to a dataframe
df_final = pd.DataFrame({
    'sentence': df['sentence'].tolist(),
    'entities': df['entities'].tolist(),
    'predicted': pred_entities
})

# Save your results
df_final.to_csv('data/results.csv', index=False)
print('your results were saved in data/results.csv')