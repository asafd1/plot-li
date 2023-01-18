import csv
import subprocess

from Constants import data_schema_prompt_format, default_data_file_path, prompt_format, plot_code_path


def read_columns_names(path=default_data_file_path):
    with open(path, 'r') as f:
        d_reader = csv.DictReader(f)
        column_names = d_reader.fieldnames
        return ",".join(column_names)


def get_init_prompt(path=default_data_file_path):
    columns = read_columns_names(path)
    return data_schema_prompt_format.format(columns)


def get_wrapped_prompt(user_prompt, path=default_data_file_path):
    return prompt_format.format(path, user_prompt)

if __name__ == '__main__':
    print(get_init_prompt())
    print(get_wrapped_prompt("How many organizations of type PAID are there in each location"))
    subprocess.call(['python3', plot_code_path])
