from django.shortcuts import render
from .models import photososi
import uuid
import json
from yookassa import Configuration, Payment
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import smtplib
from email.mime.text import MIMEText
Configuration.account_id = "952391"
Configuration.secret_key = "test_Bmw6bCyD2FXQI62CmoBxGtUeUq0F8CVi-hcfYeOmtEo"



def otpravson():
    message=''
    sender = 'abdulaziz0102007@gmail.com'
    password = 'ouzouxyzrtchsjah'
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(sender,password)
    file=open('mainpage/ss.txt',"r",encoding="utf-8")
    for i in file.readlines():
        message+=i+"\n"
    message = MIMEText(message, 'plain', 'utf-8')
    file.close()
    server.sendmail(sender,"abdulaziz01022007@gmail.com",message.as_string())

def homepage(request):

    
    return render(request, 'mainpage/home.html')
def korzina(request):
    return render(request, 'mainpage/korz.html')
def otmena(request):
    return render(request, 'mainpage/otmen.html')
def nravit(request):
    return render(request, 'mainpage/nravit.html')
def photo(request):
    mebeli=photososi.objects.all()
    return render(request, 'mainpage/photo.html',{'mebeli': mebeli})
def oplata(request):
    lol=''
    try:
        i=eval(str(request.GET.get('zakazi'))) 
        for x in i:
            lol+=x+"\n"
    except:
        i1=eval(str(request.GET.get('zakazi1')))
        for x in  i1:
            lol+=x+"\n"
    file=open('mainpage/ss.txt','w',encoding='utf-8')
    file.write("""
    имя :"""+str(request.GET.get('imya_polzovatelya'))+"""
    цена :"""+str(request.GET.get('obj_tsen'))+"""
    номер телефона :"""+str(request.GET.get('teleph_num'))+"""
    адрес :"""+str(request.GET.get('adress'))+"""
    примечания :"""+str(request.GET.get('primech'))+str(request.GET.get(''))+"""
    заказы :"""+lol+"""
    """)
    file.close()
      
    try:
        payment = Payment.create({
        "amount": {
            "value": request.GET.get('obj_tsen'),
            "currency": "RUB"
        },
        "confirmation": {
            "type": "redirect",
            "return_url": "http://azizsup.pythonanywhere.com/otmena"
        },
        "description": "..."
        }, uuid.uuid4())
        return HttpResponseRedirect(payment.confirmation.confirmation_url)
    except:
        payment = Payment.create({
        "amount": {
            "value": request.GET.get('obj_tsen1'),
            "currency": "RUB"
        },
        "confirmation": {
            "type": "redirect",
            "return_url": "http://azizsup.pythonanywhere.com/otmena"
        },
        "description": "..."
        }, uuid.uuid4())
        return HttpResponseRedirect(payment.confirmation.confirmation_url)
class YandexNotifications(APIView):
    permission_classes = (AllowAny)

    
    @csrf_exempt
    def post(request):    
        json_data = json.loads(request.body)
        payment_id= json_data['object']['id']
        Payment.capture(payment_id)
        otpravson()
        return HttpResponse(status=200)

