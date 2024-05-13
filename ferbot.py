import google.generativeai as genai
import os

GOOGLE_API_KEY = 'YOUR_KEY_HERE'
genai.configure(api_key=GOOGLE_API_KEY)

gen_config = {
    'candidate_count': 1,
    'temperature': 0.5
}

safety_config = {
    'harassment': 'block_none',
    'hate': 'block_none',
    'sexual': 'block_none',
    'dangerous': 'block_none'
}

model = genai.GenerativeModel(model_name='gemini-1.0-pro',
                              generation_config=gen_config,
                              safety_settings=safety_config)

chat = model.start_chat(history=[])

os.system('clear')

print('\n❰F❱❰E❱❰R❱❰B❱❰O❱❰T❱\n')

hello = ('Responda com uma saudação informal e despojada para o usuário, faça o uso de algumas gírias. Seu nome agora é FerBot, se' 'apresente brevemente ao usuário e cite algumas de suas habilidade e encoraje o usuário a lhe fazer perguntas dos temas mais variados')

response = model.generate_content(hello)
print(f'🤖 {response.text}')

prompt = input('\n🤖 Faça a sua pergunta: ')

if prompt == 'FerBot':
    response = model.generate_content('Responda com poucas palavras como se alguém estisse te chamando, seja direto')
    print(f'\n{response.text} \n')

while prompt != 'bye' and prompt != 'BYE':
  
  if prompt == 'FerBot':
    response = model.generate_content('Responda como se alguém estisse te chamando')
    print(f'\n🤖 {response.text} \n')
  else:   
    response = chat.send_message(prompt + 'Seja objetivo nas respostas')
    print(f'\n🤖 Resposta: {response.text} \n')
  
  for c in prompt:
    print('*', end='')

  print('\n')
  prompt = input('🤖 Faça a sua pergunta: ')

response = model.generate_content('Escreva uma breve frase de despedida')

if chat.history != []:
  print(f'\n🤖 {response.text} \n')
else:  
  print(f'\n🤖 Bye! Que pena que não conversamos\n')
