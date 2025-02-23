# Calling the API Key
from dotenv import find_dotenv, load_dotenv
_ = load_dotenv(find_dotenv())
import openai

client = openai.Client()

# Building the Start Menu
print('\t**** Welcome to the @Evangelistta7 ChatBot ****')
print('\t\t** powered by gpt-4o-mini **\n')

print('Type your message bellow:                    [Enter 0 to Stop]\n')

# Starting the list
msg = []

# Loop
while True:

    msg_user = input('\nUser: ')
    msg.append({'role': 'user', 'content': msg_user})

    if msg_user.isdigit() and int (msg_user) == 0:
        print('Evangelistta7: See you later! :)')
        break # encerra 

    # API Request
    def chat(msg, model='gpt-4o-mini', max_tokens=170, temperature=0.7):
        answer = client.chat.completions.create(
        messages=msg,
        model=model,
        max_tokens=max_tokens,
        temperature=temperature,
        stream=True
        )

        answer_txt = ""

        print('Evangelistta7: ', end='')
        for stream_answer in answer:
            text = stream_answer.choices[0].delta.content
            if text:
                answer_txt += text
                print(text,end='')
        
        msg.append({'role': 'assistant', 'content': answer_txt})

        return msg
    
    chat(msg)