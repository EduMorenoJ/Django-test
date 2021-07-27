import pandas as pd


def group_by_title_and_iswc_and_remove_duplicates(path_to_file):
    df = pd.read_csv(path_to_file)
    df['contributors'] = df['contributors'].apply(lambda row: row.split('|'))
    df = df.groupby(['title','iswc'], sort=False).agg(lambda x: list(set(z for y in x for z in y)))
    return df.to_dict()

def list_to_postgres_format_list(list):
    return f'{list}'.replace('[','{').replace(']','}')