'''
Created on 16-Apr-2018

@author: kkund
'''
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
import json

from .chatbot_impl import plm_chat_bot as bot

#old chat ui
def index(request):
    #return HttpResponse("<h1>index page</h1>")
    return render(request, 'chatbot/index.html')
#new chat UI 
def chat(request):
    return render(request,'chatbot/chat.html')

@api_view(['POST'])
def chat_api(request):
    if request.method == 'POST':
        #b = bot('PLM BOT')
        body_unicode = request.body.decode('utf-8')
        get_value= json.loads(body_unicode)
        print(get_value)
        request_message = get_value['req_msg']
        print(request_message)
        # Do your logic here coz you got data in `get_value`
        data = {}
        data['result'] = 'SUCCESS'
        data['response'] = str(bot.generate_response(request_message))
        return HttpResponse(json.dumps(data), content_type="application/json")
  
    print('chat received');