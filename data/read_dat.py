import pandas as pd
import ast

list_files = ['./data/resolved_data_22-Aug-2023-1030.dat',
                "./data/crosschecked_data_22-Aug-2023-1030.dat"]

data = pd.read_csv(list_files[0], delimiter='|', header=None,
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


print(f"data: {data.shape}")
for col in ['sentence', 'classes', 'indexes']:
    if col == "classes":
        data[col] = data[col].apply(safe_eval_list)
    elif col == "indexes":
        data[col] = data[col].apply(lambda x: ast.literal_eval(x.strip()) if isinstance(x, str) else x)
        data[col] = data[col].apply(
            lambda x: {'entities': [tuple(entity) for entity in x['entities'] if isinstance(entity, list)]} if isinstance(x, dict) else x)
    else:
        data[col] = data[col].apply(lambda x: x.strip() if isinstance(x, str) else x)

print(data.head(3))

# data.to_csv('./data/output.csv', index=False)

# Flatten all the lists in the 'classes' column into a single list
entities = [item[1] for sublist in data['classes'] for item in sublist]
unique_values = list(set(entities))

print(unique_values)

list_of_tuples = list(zip(data['sentence'], data['indexes']))
# print(list_of_tuples)
