from home_page.system_instuctions import system_prompt


with open('ReCallForge informations', 'r', encoding='utf-8') as f:
    informations = f.read()

conversation_history = [
    {'role': 'system', 'content': system_prompt},
    {'role': 'user', 'content': f'This is the user informations: {informations}'}
]