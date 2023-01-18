from flask import Flask, request, render_template
from revChatGPT.ChatGPT import Chatbot

from DataUtil import get_init_prompt, get_wrapped_prompt
from PlotliLogic import process_prompt, get_plot_html
import os;
import shutil

app = Flask(__name__)

# export SESSION_TOKEN="your token"

SESSION_TOKEN = os.getenv("SESSION_TOKEN")
conversation_id = None
parent_id = None
chatbot: Chatbot

is_first_prompt_received = False


def init_server():
    global conversation_id, parent_id, chatbot
    chatbot = Chatbot({
        "session_token": SESSION_TOKEN
    }, conversation_id=None, parent_id=None)

    response = chatbot.ask(get_init_prompt())
    conversation_id = response['conversation_id']
    parent_id = response['parent_id']


@app.route('/')
def index():
    return render_template('index.html')

count = 0;
@app.route('/plot', methods=['POST'])
def get_plot():
    global conversation_id, parent_id, is_first_prompt_received, count
    user_prompt = request.get_data().decode()
    if not is_first_prompt_received:
        user_prompt = get_wrapped_prompt(user_prompt)
        print("wrapped_prompt="+user_prompt)
        is_first_prompt_received = True
    exec_result, conversation_id, parent_id = process_prompt(chatbot, user_prompt, conversation_id, parent_id)
    target_file = 'static/plot_{}.html'.format(count)
    count = count+1
    try:
       shutil.move('plot.html', target_file)
    except:
        target_file = "file_not_found.error"
    return target_file

@app.route('/reset', methods=['POST'])
def reset_chat():
    global is_first_prompt_received
    is_first_prompt_received = False
    return ""


# if __name__ == '__main__':
init_server()
app.run()
