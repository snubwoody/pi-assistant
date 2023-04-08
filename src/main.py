import openai
from audio import listen
from audio import speak


def gpt(chat_prompt:str):
    api_key:str = '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'

    openai.api_key = api_key
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

