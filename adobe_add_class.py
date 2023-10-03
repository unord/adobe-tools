from tools import *
import shutil


def move_files() -> None:
    file_list = filename_list_with_extension('csv_import', 'csv')

    for file in file_list:
        shutil.move(file, './csv_export')

def studsys_import_csv_files() -> None:
    file_list = filename_list_with_extension('csv_import', 'csv')

    for file in file_list:
        csv_clean_to_comma(file)
        csv_add_column_with_fixed_variable(file, 'Identity Type', 'Business ID')
        csv_add_column_with_fixed_variable(file, 'Domain', 'unord.dk')
        csv_duplicate_column(file, 'Mailadresse', 'Username')
        csv_rename_column(file,  ['First Name', 'Last Name', 'Email', 'Identity Type', 'Domain', 'Username'])
        csv_reorder_column(file, ['Identity Type', 'Username', 'Domain', 'Email', 'First Name', 'Last Name'])





def main():
    studsys_import_csv_files()
    move_files()


if __name__ == '__main__':
    main()




