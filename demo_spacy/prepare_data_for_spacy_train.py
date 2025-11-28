import pandas as pd
from helper_functs import fix_dataframe, convert_to_spacy, from_json_to_prevspacy, get_train_test_val
import os
from concurrent.futures import ProcessPoolExecutor
import itertools

# Load .dat files
dat_file1 = pd.read_csv("./data/crosschecked_data_22-Aug-2023-1030.dat", delimiter='|', header=None,
                   names=["classes", "sentence", "indexes"])

dat_file2 = pd.read_csv('./data/resolved_data_22-Aug-2023-1030.dat', delimiter='|', header=None,
                   names=["classes", "sentence", "indexes"])

# clean some empty values
dat_file1 = fix_dataframe(dat_file1)
dat_file2 = fix_dataframe(dat_file2)

# if you want to see entities in both .dat files
entities_train = [item[1] for sublist in dat_file1['classes'] for item in sublist]
entities_val = [item[1] for sublist in dat_file2['classes'] for item in sublist]
unique_values_1 = list(set(entities_train))
unique_values_2 = list(set(entities_val))
print(f"Available entities in dat_file1: {unique_values_1}")
print(f"Available entities in dat_file2: {unique_values_2}")

# Give proper format
DAT_FILE1 = list(zip(dat_file1['sentence'], dat_file1['indexes']))
DAT_FILE2 = list(zip(dat_file2['sentence'], dat_file2['indexes']))

# Load TAGGED JSON file
folder = "/conf/pis_di_parser/data/tagged data"
file_paths = [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith(".json")]
print(f"there are {len(file_paths)} JSON files")

# Read and get data
with ProcessPoolExecutor() as executor:
    results = list(executor.map(from_json_to_prevspacy, file_paths))

# Merge all JSON content
merged = [item for sublist in results for item in sublist]
print(f"Elements in all JSON {len(merged)}")
# Merge with those dat file content
merged_list = list(itertools.chain(merged, DAT_FILE1, DAT_FILE2))
print(f"Total elements {len(merged_list)}")
# let's check available entities
entities_list = [item[2] for sublist in merged_list for item in sublist[1].get("entities")]
unique_values = list(set(entities_list))
print(f"Total available entities: {unique_values}")

# Split into 3 datasets
TRAIN, VAL, TEST = get_train_test_val(merged_list)
print(f"TRAIN length {len(TRAIN)}")
print(f"VAL length {len(VAL)}")
print(f"TEST length {len(TEST)}")

# Convert to spacy format as a requirement to train spacy models
convert_to_spacy(TRAIN, 'train')
convert_to_spacy(VAL, 'dev')

# Save test part in a CSV file
df_test = pd.DataFrame(TEST)
df_test.rename(columns={0: 'sentence', 1: 'entities'}, inplace=True)
df_test.to_csv('data/test.csv', index=False)

# df_test = pd.DataFrame(TRAIN)
# df_test.rename(columns={0: 'sentence', 1: 'entities'}, inplace=True)
# df_test.to_csv('data/TRAIN.csv', index=False)

# df_test = pd.DataFrame(VAL)
# df_test.rename(columns={0: 'sentence', 1: 'entities'}, inplace=True)
# df_test.to_csv('data/VAL.csv', index=False)