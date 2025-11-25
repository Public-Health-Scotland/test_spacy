# Load required packages
# from spacy.training.example import Example
import pandas as pd
from helper_functs import fix_dataframe, convert_to_spacy, from_json_to_prevspacy, get_train_test_val
import os
from concurrent.futures import ProcessPoolExecutor
import itertools

# Load Custon data
train_data = pd.read_csv("./data/crosschecked_data_22-Aug-2023-1030.dat", delimiter='|', header=None,
                   names=["classes", "sentence", "indexes"])

val_data = pd.read_csv('./data/resolved_data_22-Aug-2023-1030.dat', delimiter='|', header=None,
                   names=["classes", "sentence", "indexes"])

train_data = fix_dataframe(train_data)
val_data =fix_dataframe(val_data)

print(f"train data size: {train_data.shape}")
print(f"validation data size: {val_data.shape}")
# uncomment if you want to see data in a csv format
# train_data.to_csv('data/train.csv', index=False)
# val_data.to_csv('data/val.csv', index=False)

entities_train = [item[1] for sublist in train_data['classes'] for item in sublist]
entities_val = [item[1] for sublist in val_data['classes'] for item in sublist]
unique_values_train = list(set(entities_train))
unique_values_val = list(set(entities_val))
print(f"These are the available entities in train: {unique_values_train}")
print(f"These are the available entities in test: {unique_values_val}")

TRAIN_DATA = list(zip(train_data['sentence'], train_data['indexes']))
VAL_DATA = list(zip(val_data['sentence'], val_data['indexes']))

folder = "/conf/pis_di_parser/data/tagged data"
file_paths = [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith(".json")]


# MY_DATA = from_json_to_prevspacy('data/dose_instructions_1_mm_part1.json')
print(f"there are {len(file_paths)} files")

# Step 2: Run in parallel
with ProcessPoolExecutor() as executor:
    results = list(executor.map(from_json_to_prevspacy, file_paths))

merged = [item for sublist in results for item in sublist]
print(f"number of elements {len(merged)}")
merged_list = list(itertools.chain(merged, TRAIN_DATA, VAL_DATA))
print(f"number of elements {len(merged_list)}")

TRAIN, VAL, TEST = get_train_test_val(merged_list)
print(f"TRAIN length{len(TRAIN)}")
print(f"VAL length{len(VAL)}")
print(f"TEST length{len(TEST)}")

convert_to_spacy(TRAIN, 'train')
convert_to_spacy(VAL, 'dev')

df_test = pd.DataFrame(TEST)
df_test.rename(columns={0: 'sentence', 1: 'entities'}, inplace=True)
df_test.to_csv('data/test.csv', index=False)

# df_test = pd.DataFrame(TRAIN)
# df_test.rename(columns={0: 'sentence', 1: 'entities'}, inplace=True)
# df_test.to_csv('data/TRAIN.csv', index=False)

# df_test = pd.DataFrame(VAL)
# df_test.rename(columns={0: 'sentence', 1: 'entities'}, inplace=True)
# df_test.to_csv('data/VAL.csv', index=False)

# convert_to_spacy(merged, 'total')
# # Load blank model
# nlp = spacy.blank("en")

# # Add NER pipeline
# ner = nlp.add_pipe("ner")

# # Add unique labels to the ner pipeline
# for unique in unique_values:
#     ner.add_label(unique)

# print(type(TRAIN_DATA))








# # Training loop
# optimizer = nlp.begin_training()
# for i in range(20):
#     for text, annotations in TRAIN_DATA:
#         example = Example.from_dict(nlp.make_doc(text), annotations)
#         nlp.update([example], sgd=optimizer)

# # Save the model
# nlp.to_disk("./ner_dose_model")
# print("task completed!")