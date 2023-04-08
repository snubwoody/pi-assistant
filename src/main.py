import openai
from audio import listen
from audio import speak
import json



    


def gpt(chat_prompt:str):
    with open('private.json') as f:
        obj = json.load(f)
        apikey = obj['apikey']
    openai.api_key = apikey
    response = openai.Completion.create(model="text-davinci-003", prompt=chat_prompt, temperature=0.2, max_tokens=50)
    return response.choices[0].text

#TODO find out whats taking so long
def main():
    activation_word = 'computer'
    while True:
        audio = listen()
        if audio != None:
            query = audio.lower().split()    

            if query[0] == activation_word:
                speak('how may i help you')
                instructions = listen()
                query.pop(0)
                speak(gpt(str(instructions)))

main()

