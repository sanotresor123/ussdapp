import africastalking
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# Create your views here.

@csrf_exempt
def ussd(request):
    if request.method == "POST":
        session_id = request.POST.get("sessionId", None)
        service_code = request.POST.get("serviceCode", None)
        phone_number = request.POST.get ("phoneNumber", None)
        text = request.POST.get("text", "default")
        response = ""
        if text == '':
            response = "CON Welcome to mobile money \n"
            response += "1. send money \n"
            response += "2. buy airtime \n"
            response += "3. pay bills \n"
            response += "4. bank services \n"
            response += "5. mocach \n"
        elif text == '1':
            response = "CON send money to your friend \n"
            response += "1. MOMO user \n"
            response += "2. send to ecash \n"
            response += "3. across the board \n"
            response += "4. cancel \n"
        elif text == '1*1':
            response = "CON welcome to momo user \n"  
            response += "list of users"
            return HttpResponse(response)   
        return HttpResponse(response)  
            

