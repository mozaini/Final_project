import pandas as pd


def reshape(data, variabl_name, column_name):
    dataset = pd.melt(data, id_vars=data.columns[:4],
                        value_vars=data.columns[4:],
                        var_name=variabl_name,
                        value_name=column_name)
    return dataset