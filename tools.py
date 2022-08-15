import os
import pandas as pd
import sys

## Add a column to a csv file
def csv_add_column_with_fixed_variable(file_name :str, column_name :str, column_data :str):
    try:
        df = pd.read_csv(file_name)
    except Exception as e:
        print(e)
        print(f"Could not read csv file: {file_name}")
        sys.exit()
    df[column_name] = column_data
    df.to_csv(file_name, index=False)

## clean csv file by replaceing ";" with ","
def csv_clean_to_comma(file_name :str):
    text_file_find_replace(file_name, ';', ',')
    text_file_find_replace(file_name, ', skole', '')
    text_file_find_replace(file_name, '>', '')
    text_file_find_replace(file_name, '<', '')
    text_file_find_replace(file_name, 'å', 'aa')
    text_file_find_replace(file_name, 'ø', 'oe')
    text_file_find_replace(file_name, 'æ', 'ae')
    text_file_find_replace(file_name, 'Ø', 'Oe')
    text_file_find_replace(file_name, 'Æ', 'Ae')
    text_file_find_replace(file_name, 'Å', 'Aa')
    text_file_find_replace(file_name, 'é', 'e')
    text_file_find_replace(file_name, 'á', 'a')
    text_file_find_replace(file_name, 'ü', 'u')
    text_file_find_replace(file_name, 'í', 'i')
    text_file_find_replace(file_name, 'ä', 'a')

def csv_drop_rows_if_string_length_is_less_than(file_name :str, column_name :str, length :int):
    df = pd.read_csv(file_name)
    df = df[df[column_name].str.len() > length]
    df.to_csv(file_name, index=False)

def csv_drop_rows_if_string_contains(file_name :str, column_name :str, search_for :list):
    df = pd.read_csv(file_name)
    df = df[~df[column_name].str.contains('|'.join(search_for))]
    df.to_csv(file_name, index=False)

def csv_duplicate_column(file_name :str, column_name :str, new_column_name :str):
    df = pd.read_csv(file_name)
    df[new_column_name] =  df[column_name]
    df.to_csv(file_name, index=False)


## remove a column from a csv file
def csv_remove_colomn(file_name :str, column_name :str):
    df = pd.read_csv(file_name)
    df.drop(column_name, axis=1, inplace=True)
    df.to_csv(file_name, index=False)


## csv file rename columns
def csv_rename_column(file_name :str, column_name :list):
    df = pd.read_csv(file_name)
    df.columns = column_name
    df.to_csv(file_name, index=False)

##
def csv_file_value_not_in_other_file(file_name :str, column_name :str, other_file_name :str, list_filename :str):
    df = pd.read_csv(file_name)
    other_df = pd.read_csv(other_file_name)

    common = other_df.merge(other_df, on=[column_name])
    result = df[~df.Email.isin(common.Email)]
    result.to_csv(list_filename, index=False)


## csv reorder columns
def csv_reorder_column(file_name :str, column_order :list):
    df = pd.read_csv(file_name)
    df = df[column_order]
    df.to_csv(file_name, index=False)


## Use find and replace in a text file
def text_file_find_replace(file_name :str, search_for :str, replace_with :str):
    with open(file_name, 'r') as file:
        data = file.read()
        data = data.replace(search_for, replace_with)
        with open(file_name, 'w') as file:
            file.write(data)

def file_to_utf8(file_name :str):
    with open(file_name, 'r', encoding="utf-8", errors='replace') as file:
        data = file.read()
        with open(file_name, 'w', encoding="utf-8") as file:
            file.write(data)

## Retrives the file names in a directory
def filename_list_with_extension(directory: str, extension: str):
    filename_list = []
    for file in os.listdir(f"./{directory}"):
        if file.endswith(f".{extension}"):
            filename_list.append(f"./{directory}/"+file)
    return filename_list





def main():
    pass

if __name__ == '__main__':
    main()

