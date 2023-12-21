
import pandas as pd
import numpy as np

def column_rename (df: pd.DataFrame) -> pd.DataFrame:
    """
    This function renames column names by removing spaces and converting to lower case
    Inputs: df of type pandas dataframe
    Outputs: returns the dataframe with the renamed columns
    """
    cols =[]
    for x in df.columns:
        if isinstance(x, str):
            cols.append(x.lower().replace(' ', '_'))
        else:
            cols.append(x)
            
    df.columns=cols
    return df



def col_replace_dash (df: pd.DataFrame) -> pd.DataFrame:
    """
    This function renames column names by removing spaces and converting to lower case
    Inputs: df of type pandas dataframe
    Outputs: returns the dataframe with the renamed columns
    """
    cols =[]
    for x in df.columns:
        if isinstance(x, str):
            cols.append(x.lower().replace('-', '_'))
        else:
            cols.append(x)
            
    df.columns=cols
    return df



def clean_agency_name (df: pd.DataFrame) -> pd.DataFrame:
    """
    This function groups the same values of the agency name column
    It uses a dictionary to replace the redundant values
    Inputs: df type pandas dataframe
    Outputs: returns the dataframe with the renamed columns
    """
    new_row_values = {'montgomery county police': 'montgomery', 'rockville police departme' : 'rockville', 'gaithersburg police depar' : 'gaithersburg',
    'takoma park police depart': 'takoma', 'maryland-national capital': 'maryland'}
    df['agency_name']= df['agency_name'].replace(new_row_values)
    return df


def clean_collision_type(df: pd.DataFrame) -> pd.DataFrame:
    """
    This function renames the clean collision type column
    It uses combination of regex and a dictionary to do so
    Inputs: df of type pandas dataframe
    Outputs: returns the dataframe with the renamed values
    """
    replace_short= {'\\bdir\\b' : 'direction', '\\brend\\b' : 'rear end'}
    df['collision_type']= df['collision_type'].replace(replace_short, regex=True)
    return df
    
    
def df_to_lower (df: pd.DataFrame) -> pd.DataFrame:
    """
    This function converts all the values in all the columns to lower case
    Inputs: df of type pandas dataframe
    Outputs: returns the dataframe with the string values in lower case
    """
    df = df.map(lambda x: x.lower() if isinstance(x, str) else x)
    return df


def replace_invalids_of_column(df: pd.DataFrame, num_replacements: float, replacement_value:str, col_to_clean: str) -> pd.DataFrame:
    """
    This function removes the invalid values from the given column
    Inputs: df of type pandas dataframe, the values that will replace the invalid values, and their frequencies
    Outputs: returns dataframe with the replaced invalid values
    """
    invalid_indices= df[df[col_to_clean] == 'invalid'].index
    selected_indices = np.random.choice(invalid_indices, size=num_replacements, replace=False)
    df.loc[selected_indices, col_to_clean] = replacement_value
    return df
