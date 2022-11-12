from django.shortcuts import render, get_object_or_404
from .models import Mebel,Stulia,Barnie_stulya,Stoli,Divani,Crovati,Cresla
# Create your views here.


def stulia(request):
    mebeli=[]
    if not request.GET.get('tsena_min'):
        for i in Stulia.objects.all():
            if str(i.title).lower().find(str(request.GET.get('poisk',"")).lower())!=-1:
                mebeli.append(i)
    
    else:    
        for i in Stulia.objects.all():
            if i.price in range(int(request.GET.get('tsena_min')),int(request.GET.get('tsena_max'))):
                if request.GET.get('Plastic') and i.Plastic:
                    mebeli.append(i)
                elif request.GET.get('Tkan') and i.Tkanini:
                    mebeli.append(i)
                elif request.GET.get('EcoKoja') and i.EcoKoja:
                   mebeli.append(i)
                if request.GET.get('ObivkaPach') and i.ObivPecg:
                   mebeli.append(i)
                elif request.GET.get('PovKres') and i.PovCresl:
                   mebeli.append(i)
                elif request.GET.get('DerevyanOsn') and i.DerevOsn:
                   mebeli.append(i)
                     

    return render(request, 'mebel/stulia.html',{'mebeli': mebeli})
def stoli(request):
    mebeli=[]
    if not request.GET.get('tsena_min'):
        for i in Stoli.objects.all():
            if str(i.title).lower().find(str(request.GET.get('poisk',"")).lower())!=-1:
                mebeli.append(i)
    
    else:    
        for i in Stoli.objects.all():
            if i.price in range(int(request.GET.get('tsena_min')),int(request.GET.get('tsena_max'))):
                if int(i.dlina) in range (int(request.GET.get('min_dlina'))+1,int(request.GET.get('max_dlina'))+1):
                    if request.GET.get('Raskladnie') and i.raskladnoy:
                        if  request.GET.get('TRANFORMERSMORETHANMEETSTHEEIE') and i.Stul_transformer:mebeli.append(i)
                        elif  request.GET.get('KruglStul') and i.Krug:mebeli.append(i)
                        elif  request.GET.get('OvalStol') and i.Oval:mebeli.append(i)
                        elif  request.GET.get('PryamUgolStol') and i.PryamoUg:mebeli.append(i)
                        elif  request.GET.get('SKeramicPocr') and i.SoStecl:mebeli.append(i)
                        elif  request.GET.get('SoSteclom') and i.SKeramPok:mebeli.append(i)
                        elif  request.GET.get('JurnalStol') and i.JoutStoul:mebeli.append(i)
                        else:mebeli.append(i)    

                    elif request.GET.get('NeRaskladnie') and i.neraskladnoy:
                        if  request.GET.get('TRANFORMERSMORETHANMEETSTHEEIE') and i.Stul_transformer:mebeli.append(i)
                        elif  request.GET.get('KruglStul') and i.Krug:mebeli.append(i)
                        elif  request.GET.get('OvalStol') and i.Oval:mebeli.append(i)
                        elif  request.GET.get('PryamUgolStol') and i.PryamoUg:mebeli.append(i)
                        elif  request.GET.get('SKeramicPocr') and i.SoStecl:mebeli.append(i)
                        elif  request.GET.get('SoSteclom') and i.SKeramPok:mebeli.append(i)
                        elif  request.GET.get('JurnalStol') and i.JoutStoul:mebeli.append(i)
                        else:mebeli.append(i)  
                   
                elif int(i.diametr) in range (int(request.GET.get('min_dlina'))+1,int(request.GET.get('max_dlina'))+1): 
                    if request.GET.get('Raskladnie') and i.raskladnoy:
                        if  request.GET.get('TRANFORMERSMORETHANMEETSTHEEIE') and i.Stul_transformer:mebeli.append(i)
                        elif  request.GET.get('KruglStul') and i.Krug:mebeli.append(i)
                        elif  request.GET.get('OvalStol') and i.Oval:mebeli.append(i)
                        elif  request.GET.get('PryamUgolStol') and i.PryamoUg:mebeli.append(i)
                        elif  request.GET.get('SKeramicPocr') and i.SoStecl:mebeli.append(i)
                        elif  request.GET.get('SoSteclom') and i.SKeramPok:mebeli.append(i)
                        elif  request.GET.get('JurnalStol') and i.JoutStoul:mebeli.append(i)
                        else:mebeli.append(i)    

                    elif request.GET.get('NeRaskladnie') and   i.neraskladnoy:
                        if  request.GET.get('TRANFORMERSMORETHANMEETSTHEEIE') and i.Stul_transformer:mebeli.append(i)
                        elif  request.GET.get('KruglStul') and i.Krug:mebeli.append(i)
                        elif  request.GET.get('OvalStol') and i.Oval:mebeli.append(i)
                        elif  request.GET.get('PryamUgolStol') and i.PryamoUg:mebeli.append(i)
                        elif  request.GET.get('SKeramicPocr') and i.SoStecl:mebeli.append(i)
                        elif  request.GET.get('SoSteclom') and i.SKeramPok:mebeli.append(i)
                        elif  request.GET.get('JurnalStol') and i.JoutStoul:mebeli.append(i)
                        else:mebeli.append(i)  
                    else:mebeli.append(i)                    

    return render(request, 'mebel/stoli.html',{'mebeli': mebeli})
def barnie_stulya(request):
    
    mebeli=[]
   
    if not request.GET.get('tsena_min'):
        for i in Barnie_stulya.objects.all():
            if str(i.title).lower().find(str(request.GET.get('poisk',"")).lower())!=-1:
                mebeli.append(i)
    
    else:
        for i in Barnie_stulya.objects.all():
            if i.price in range(int(request.GET.get('tsena_min')),int(request.GET.get('tsena_max'))):
                if request.GET.get('barnie_stulya') and i.barStul:
                    mebeli.append(i)
                if request.GET.get('polubarnie_stulya') and i.polubarStul:
                    mebeli.append(i)                
                if request.GET.get('visota_reg') and i.SRegulVisot:
                    mebeli.append(i)

     
    return render(request, 'mebel/barnie_stulya.html',{'mebeli': mebeli})
def cresla(request):

    mebeli=[]
    if not request.GET.get('tsena_min'):
        for i in Cresla.objects.all():
            if str(i.title).lower().find(str(request.GET.get('poisk',"")).lower())!=-1:
                mebeli.append(i)
    
    else:    
        for i in Cresla.objects.all():
            if i.price in range(int(request.GET.get('tsena_min')),int(request.GET.get('tsena_max'))):
                if request.GET.get('Raskladnie') and i.raskladniye:
                    if request.GET.get('Recliner') and i.reclainer:
                        mebeli.append(i)
                    elif request.GET.get('StilCounter') and i.StilContour:
                        mebeli.append(i)
                    elif request.GET.get('StilHusk') and i.StilHusk:
                        mebeli.append(i)
                    elif request.GET.get('Vtkani') and i.VTkanini:
                        mebeli.append(i)
                    elif request.GET.get('ObivkaPechwork') and i.ObivPech:
                        mebeli.append(i)
                    elif request.GET.get('PovorotnieCresla') and i.PovCresl:
                        mebeli.append(i)
                    elif request.GET.get('CreslaCrovati') and i.kresla_krovati:
                        mebeli.append(i)
                    else:mebeli.append(i)
                elif request.GET.get('NeRaskladnie') and i.neraskladniye:
                    if request.GET.get('Recliner') and i.reclainer:
                        mebeli.append(i)
                    elif request.GET.get('StilCounter') and i.StilContour:
                        mebeli.append(i)
                    elif request.GET.get('StilHusk') and i.StilHusk:
                        mebeli.append(i)
                    elif request.GET.get('Vtkani') and i.VTkanini:
                        mebeli.append(i)
                    elif request.GET.get('ObivkaPechwork') and i.ObivPech:
                        mebeli.append(i)
                    elif request.GET.get('PovorotnieCresla') and i.PovCresl:
                        mebeli.append(i)
                    elif request.GET.get('CreslaCrovati') and i.kresla_krovati:
                        mebeli.append(i)
                    else:mebeli.append(i)
                else:                   
                    if request.GET.get('Recliner') and i.reclainer:
                        mebeli.append(i)
                    elif request.GET.get('StilCounter') and i.StilContour:
                        mebeli.append(i)
                    elif request.GET.get('StilHusk') and i.StilHusk:
                        mebeli.append(i)
                    elif request.GET.get('Vtkani') and i.VTkanini:
                        mebeli.append(i)
                    elif request.GET.get('ObivkaPechwork') and i.ObivPech:
                        mebeli.append(i)
                    elif request.GET.get('PovorotnieCresla') and i.PovCresl:
                        mebeli.append(i)
                    elif request.GET.get('CreslaCrovati') and i.kresla_krovati:
                        mebeli.append(i)
    return render(request, 'mebel/cresla.html',{'mebeli': mebeli})
def crovati(request): 
    mebeli=[]
    if not request.GET.get('tsena_min'):
        for i in Crovati.objects.all():
            if str(i.title).lower().find(str(request.GET.get('poisk',"")).lower())!=-1:
                mebeli.append(i)
    
    else:    
        for i in Cresla.objects.all():
            if i.price in range(int(request.GET.get('tsena_min')),int(request.GET.get('tsena_max'))):
                if request.GET.get('SPodyomMech') and i.podmeh:
                    if request.GET.get('Vtkani') and i.vtkanini:
                        mebeli.append(i)
                    elif request.GET.get('Glyanez') and i.Glyanez:
                        mebeli.append(i)
                    else:mebeli.append(i)
                elif request.GET.get('BezPodyomMech') and i.bezpodmeh:
                    if request.GET.get('Vtkani') and i.vtkanini:
                        mebeli.append(i)
                    elif request.GET.get('Glyanez') and i.Glyanez:
                        mebeli.append(i)
                    else:mebeli.append(i)  
                else:      
                    if request.GET.get('Vtkani') and i.vtkanini:
                        mebeli.append(i)
                    elif request.GET.get('Glyanez') and i.Glyanez:
                        mebeli.append(i)
                    else:mebeli.append(i)                      
    return render(request, 'mebel/crovati.html',{'mebeli': mebeli})
def divani(request):
    mebeli=[]
    if not request.GET.get('tsena_min'):
        for i in Divani.objects.all():
            if str(i.title).lower().find(str(request.GET.get('poisk',"")).lower())!=-1:
                mebeli.append(i)
    else:    
        for i in Divani.objects.all():
            if i.price in range(int(request.GET.get('tsena_min')),int(request.GET.get('tsena_max'))):
                if request.GET.get("3xMest") and i.threex :
                    if request.GET.get("Raskladnie") and i.threex :
                       if request.GET.get("RaslaVpered") and i.raskpladVpered : mebeli.append(i)
                       elif request.GET.get("RaskladKaKnijka") and i.RasplaKaKnijka:mebeli.append(i)
                       else:mebeli.append(i)
                   
                    elif request.GET.get("NeRaskladnie") and i.nerakladniye:
                        if not (request.GET.get("RaslaVpered") and i.raskpladVpered):
                            if not (request.GET.get("RaskladKaKnijka") and i.RasplaKaKnijka):
                                mebeli.append(i)
                    else: mebeli.append(i)

                elif request.GET.get("2xMest") and i.two :
                    if request.GET.get("RaskladKaKnijka") and i.RasplaKaKnijka:mebeli.append(i)
                    elif request.GET.get("NeRaskladnie") and i.nerakladniye:mebeli.append(i)
                    else:mebeli.append(i)
                elif request.GET.get("Uglovie") and i.ugol: 
                    if not (i.RasplaKaKnijka or i.raskpladVpered or i.SDvuspalKrovat):
                        mebeli.append(i)
                    else:mebeli.append(i)
                elif request.GET.get("RaskladKaKnijka")  and i.RasplaKaKnijka:
                    if not i.nerakladniyemebeli:mebeli.append(i)
                elif request.GET.get("RaslaVpered")  and i.raskpladVpered:
                    if not i.nerakladniyemebeli:mebeli.append(i)
                elif request.GET.get("RaslaVpered")  and i.raskpladVpered:
                    if not i.nerakladniyemebeli:mebeli.append(i)
                elif request.GET.get("Raskladnie")  and i.rakladniye:mebeli.append(i)
                else:mebeli.append(i)







    return render(request, 'mebel/divani.html',{'mebeli': mebeli})
def mebels(request):
    mebeli = Barnie_stulya.objects.all()
    return render(request, 'mebel/mebels.html',{'mebeli': mebeli})
def novinki(request):
    mebeli = Barnie_stulya.objects.filter(Novinki=True)
    mebeli1 = Stulia.objects.filter(Novinki=True)
    mebeli2 = Stoli.objects.filter(Novinki=True)
    mebeli3 = Divani.objects.filter(Novinki=True)
    mebeli4 = Cresla.objects.filter(Novinki=True)
    mebeli5 = Crovati.objects.filter(Novinki=True)


    return render(request, 'mebel/novinki.html',{'mebeli': mebeli,'mebeli1': mebeli1,'mebeli2': mebeli2,'mebeli3': mebeli3,'mebeli4': mebeli4,'mebeli5': mebeli5})


def detail_barstul (request,blog_id):
    blog = get_object_or_404(Barnie_stulya,pk=blog_id)
    return render(request,'mebel/detail_barstul.html',{'blog':blog})
def detail_stul (request,blog_id):
    blog = get_object_or_404(Stulia,pk=blog_id)
    return render(request,'mebel/detail_stul.html',{'blog':blog})
def detail_stol (request,blog_id):
    blog = get_object_or_404(Stoli,pk=blog_id)
    return render(request,'mebel/detail_stoli.html',{'blog':blog})
def detail_div (request,blog_id):
    blog = get_object_or_404(Divani,pk=blog_id)
    return render(request,'mebel/detail_divani.html',{'blog':blog})
def detail_cres (request,blog_id):
    blog = get_object_or_404(Cresla,pk=blog_id)
    return render(request,'mebel/detail_cresla.html',{'blog':blog})
def detail_crov (request,blog_id):
    blog = get_object_or_404(Crovati,pk=blog_id)
    return render(request,'mebel/detail_crovati.html',{'blog':blog})
