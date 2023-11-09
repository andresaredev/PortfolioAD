# chatbot_app/views.py
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import re
import random

@csrf_exempt
def chatbot(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input', '')
        response = get_response(user_input)
        return JsonResponse({'response': response})
    return render(request, 'chatbot.html')  # Asegúrate de tener una plantilla llamada chatbot.html en tu carpeta templates/chatbot_app/


def get_response(user_input):
    split_message = re.split(r'\s|[,:;.?!-_]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

def message_probability(user_message, recognized_words, single_response=False, required_word=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognized_words:
            message_certainty +=1

    percentage = float(message_certainty) / float (len(recognized_words))

    for word in required_word:
        if word not in user_message:
            has_required_words = False
            break
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def check_all_messages(message):
        highest_prob = {}

        def response(bot_response, list_of_words, single_response = False, required_words = []):
            nonlocal highest_prob
            highest_prob[bot_response] = message_probability(message, list_of_words, single_response, required_words)

        response('Hola', ['hola', 'klk', 'saludos', 'buenas'], single_response=True)
        response('Estoy bien y tú?', ['como', 'estas', 'va', 'vas', 'sientes'], required_words=['como'])
        response('Estoy ubicado en la ciudad de Bogotá, pero amo trabajar de manera remota', ['ubicados', 'direccion', 'donde', 'ubicacion', ''], single_response=True)
        response('Siempre a la orden', ['gracias', 'te lo agradezco', 'thanks'], single_response=True)

        # Respuestas relacionadas con un portafolio profesional y contrataciones en desarrollo de software
        response('Mi salario esperado es competitivo y negociable', ['sueldo', 'salario', 'ganar', 'pago', 'pagos'])
        response('Mis habilidades de desarrollo incluyen Python, JavaScript, y más', ['habilidades', 'desarrollo', 'tecnologias'])
        response('Sí, actualmente estoy trabajando en proyectos interesantes', ['trabajas', 'empleo', 'proyectos'])
    
        # Preguntas frecuentes sobre portafolios y contrataciones
        response('Puedes revisar mi portafolio en [inserta el enlace a tu portafolio]', ['portafolio', 'trabajos', 'proyectos'])
        response('Mis proyectos anteriores incluyen [describe algunos proyectos destacados]', ['proyectos anteriores', 'experiencia'])
        response('Estoy familiarizado con [tecnologías específicas] y he trabajado en [industrias específicas]', ['tecnologias', 'industrias', 'experiencia'])
        response('¿Cuáles son tus fortalezas como desarrollador?', ['fortalezas', 'habilidades', 'destrezas'])

        best_match = max(highest_prob, key=highest_prob.get)
        #print(highest_prob)

        return unknown() if highest_prob[best_match] < 1 else best_match

def unknown():
    response = ['puedes decirlo de nuevo?', 'No estoy seguro de lo quieres', 'búscalo en google a ver que tal'][random.randrange(3)]
    return response

# while True:
#     print("Bot: " + get_response(input('You: ')))

