import pandas as pd


def reshape(data, var_name, value_name):
    pd.melt(data, id_vars=data.columns[:4],
            value_vars=data.columns[4:],
            var_name=var_name,
            value_name=value_name)
