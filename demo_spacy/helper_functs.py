import ast
import pandas as pd
from spacy.tokens import DocBin
import spacy

# Create function to prepare your custom data
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

# filter empty values
def fix_dataframe(data: pd.DataFrame) -> pd.DataFrame:
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
    
    return data

def convert_to_spacy(DATA, file_name: str):
    nlp = spacy.blank("en")
    doc_bin = DocBin()
    for text, annotations in DATA:
        doc = nlp.make_doc(text)
        ents = []
        for start, end, label in annotations["entities"]:
            # print(f"Label: {label}")
            span = doc.char_span(start, end, label=label)
            if span:
                # print(f"span: {span}")
                ents.append(span)
        doc.ents = ents
        doc_bin.add(doc)
    
    # exporting to a more efficient format
    doc_bin.to_disk(f"./data/{file_name}.spacy")