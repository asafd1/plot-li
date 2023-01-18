data_schema_prompt_format = "my data schema includes the following columns: {}"

plot_code_path = "plot_code.py"

plot_file_path = "plot.html"

default_data_file_path = "my_data.csv"

prompt_format = "I want a python3 code which uses pandas and plotly, and creates a plot using the data in the file {} " \
                "for the following task: {}. use pandas to prepare the data so the plot will be accurate. make sure " \
                "you import all the necessary packages. no other words other then the code itself are allowed in your " \
                "response. please set in the code the axes names, a legend, a plot title and save the file under the " \
                "name plot.html"
