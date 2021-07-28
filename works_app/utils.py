import pandas as pd


def group_by_title_and_iswc_and_remove_duplicates(path_to_file):
    df = pd.read_csv(path_to_file)
    df['contributors'] = df['contributors'].apply(lambda row: row.split('|'))
    df = df.groupby(['title', 'iswc'], sort=False).agg(
        lambda x: list(set(z for y in x for z in y)))
    return _format_result_df_in_list_of_dicts(df)


def _format_result_df_in_list_of_dicts(df):
    df_dict = df.to_dict()['contributors']
    return [{'title': i[0], 'iswc':i[1], 'contributors':df_dict[i]} for i in df_dict]
