from ast import literal_eval
import spacy
import pandas as pd

df = pd.read_csv("data/test.csv")
# print(df.dtypes)

nlp = spacy.load(".model/ner_dose_model/model-best")  # use the best trained weights

true_entities = []
pred_entities = []

for index, row in df.iterrows():
    doc = nlp(str(row["sentence"]))
    # , ent.text
    pred = [tuple([ent.start_char, ent.end_char, ent.label_]) for ent in doc.ents]
    print(pred)

    # Predicted entities
    # pred = [(ent.start_char, ent.end_char, ent.label_) for ent in doc.ents]
    my_dict = {"entities": pred}
    pred_entities.append(my_dict)

    # # Ground truth entities (convert string to dict if needed)
    # gt = literal_eval(row["entities"])["entities"]
    # true_entities.append(gt)

# print(true_entities)
print(pred_entities)

# final result
df_final = pd.DataFrame({
    'sentence': df['sentence'].tolist(),
    'entities': df['entities'].tolist(),
    'predicted': pred_entities
})

df_final.to_csv('data/results.csv', index=False)