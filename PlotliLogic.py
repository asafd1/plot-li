import base64
import subprocess

from revChatGPT.ChatGPT import Chatbot

from Constants import plot_code_path, plot_file_path


def clean_code(code: str):
    code_start_index = code.find('```')
    start_index = code.find('import', code_start_index)
    end_index = code.find('```', start_index)
    if start_index != -1 and end_index != -1:
        return code[start_index:end_index]
    return code


def save_code_to_file(code):
    with open(plot_code_path, 'w') as f:
        f.write(code)
    print('Code file saved!\n')


def process_prompt(chatbot: Chatbot, prompt, conversation_id=None, parent_id=None):
    tries = 3
    exec_result = 1
    while tries > 0 and exec_result != 0:
        response = chatbot.ask(prompt, conversation_id, parent_id)
        conversation_id = response['conversation_id']
        parent_id = response['parent_id']

        code = clean_code(response['message'])
        save_code_to_file(code)

        exec_result = subprocess.call(['python3', plot_code_path])
        print(f'Code execution ended with result: {exec_result}')

        tries -= 1
        prompt = "something went wrong when I executed your code. can you try again please? make sure you start the " \
                 "code with the imports and then immediately do the logic"

    return exec_result, conversation_id, parent_id


def get_plot_html(exec_result):
    if exec_result != 0:
        return "An error occurred. Please try again!"

    with open(plot_file_path, 'r') as f:
        html_string = f.read()
        enc_html = base64.b64encode(html_string.encode())
        return enc_html.decode()
