from django.shortcuts import render
from chat.scraper import save_satellites
from rag.rag import rag_db
from chat.chatservice import ChatService
from django.contrib.auth.decorators import user_passes_test
import json
from django.http import JsonResponse

chat_service = ChatService()    

def chat(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    elif request.method == "POST":
        data = json.loads(request.body)
        user_message = data.get("message", "")

        bot_response, message_history = chat_service.handle_message(user_message)

        return JsonResponse({
            "response": bot_response,
            "history": message_history
        })
    
    return JsonResponse({"error": "Método não permitido"}, status=405)

def is_admin(user):
    return user.is_superuser

@user_passes_test(is_admin)
def load_database(request):
    save_satellites()
    return render(request, 'load_database.html') 

@user_passes_test(is_admin)
def build_rag(request):
    rag_db()
    return render(request, 'build_rag.html') 


