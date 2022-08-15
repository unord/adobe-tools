from tools import *



def adobe_find_students_not_at_unord(csv_adbobe_file :str, csv_studsys_file :str):
    adobe_directory = './csv_adobe_complete/'
    adobe_delete_list = './csv_adobe_delete_list/'
    studsys_directory = './csv_studsys_complete/'

    exclude_in_email_list = ['admiko', 'reventlow', '@vordingborg-gym.dk', 'EFIF.DK', 'knord.dk', 'faaborg','VORDINGBORG-GYM.DK','adobe']

    csv_adbobe_file = adobe_directory + csv_adbobe_file
    csv_studsys_file = studsys_directory + csv_studsys_file
    adobe_delete_list = adobe_delete_list + 'students_not_at_unord.csv'

    csv_clean_to_comma(csv_studsys_file)
    file_to_utf8(csv_studsys_file)
    csv_rename_column(csv_studsys_file, ['First Name', 'Last Name', 'Email'])
    csv_file_value_not_in_other_file(csv_adbobe_file, 'Email', csv_studsys_file, adobe_delete_list)
    csv_drop_rows_if_string_length_is_less_than(adobe_delete_list, 'Email', 13)
    csv_drop_rows_if_string_contains( adobe_delete_list, 'Email', exclude_in_email_list)



def main():
    adobe_find_students_not_at_unord('users.csv', 'Export.csv')


if __name__ == '__main__':
    main()

