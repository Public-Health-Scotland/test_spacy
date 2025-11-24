
from spacy.scorer import Scorer
from spacy.training import Example
import spacy
import pandas as pd
from ast import literal_eval

df = pd.read_csv("data/test.csv")
nlp = spacy.load(".model/ner_dose_model/model-best")  # use the best trained weights

scorer = Scorer()
for _, row in df.iterrows():
    text = row["sentence"]
    doc_pred = nlp(text)
    pred = [tuple([ent.start_char, ent.end_char, ent.label_]) for ent in doc_pred.ents]
    # Ground truth
    # doc_true = nlp.make_doc(text)
    example = Example.from_dict(pred, literal_eval(row["entities"]["entities"]))
    scorer.score(example)

print(scorer.score)
