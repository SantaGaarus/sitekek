from django.db import models

class Mebel(models.Model):
    title = models.CharField("название ", max_length=150)
    price = models.IntegerField("цена")
    image = models.ImageField(upload_to='mebel/images/')
    image1 = models.ImageField(upload_to='mebel/images/')
    image2 = models.ImageField(upload_to='mebel/images/')
    image3 = models.ImageField(upload_to='mebel/images/')
    image4 = models.ImageField(upload_to='mebel/images/')
    image5 = models.ImageField(upload_to='mebel/images/')
    def __str__(self):
        return self.title
class Barnie_stulya(models.Model):
    title = models.CharField("название ", max_length=150)
    price = models.IntegerField("цена")

    image = models.ImageField(upload_to='mebel/images/')
    image1 = models.ImageField(upload_to='mebel/images/')
    image2 = models.ImageField(upload_to='mebel/images/')
    image3 = models.ImageField(upload_to='mebel/images/')
    image4 = models.ImageField(upload_to='mebel/images/')
    image5 = models.ImageField(upload_to='mebel/images/')
    width_stul =  models.CharField("Ширина сиденья", max_length=150)
    deep_stul =  models.CharField("Глубина общая", max_length=150)
    depp_sid =  models.CharField("Глубина сиденья", max_length=150)
    height_obj =  models.CharField("Высота общая", max_length=150)
    height_stul =  models.CharField("Высота сиденья", max_length=150)
    obivka = models.CharField("Обивка ", max_length=150)
    nojki = models.CharField("Ножки ", max_length=150)
    description = models.TextField("Описание", max_length=10000)
    barStul= models.BooleanField("Барные стулья")
    polubarStul= models.BooleanField("Полубарные стулья")
    SRegulVisot= models.BooleanField("С регулировкой высоты")
    Novinki= models.BooleanField("Новинки")
    def __str__(self):
        return self.title

class Cresla(models.Model):
    title = models.CharField("название ", max_length=150)
    price = models.IntegerField("цена(вместе с оттоманкой)")
    image = models.ImageField(upload_to='mebel/images/')
    image1 = models.ImageField(upload_to='mebel/images/')
    image2 = models.ImageField(upload_to='mebel/images/')
    image3 = models.ImageField(upload_to='mebel/images/')
    image4 = models.ImageField(upload_to='mebel/images/')
    width =  models.CharField("Ширина", max_length=150)
    deep =  models.CharField("Глубина", max_length=150)
    height_obj =  models.CharField("Высота общая", max_length=150)
    height_sid =  models.CharField("Высота сиденья", max_length=150)
    ott_dlin =  models.CharField("Длина оттоманки", max_length=150)
    ott_width =  models.CharField("Ширина оттоманки", max_length=150)
    height_ott =  models.CharField("Высота оттоманки", max_length=150)
    obivka = models.CharField("Обивка ", max_length=150)
    nojki = models.CharField("Ножки ", max_length=150)
    napolnitel = models.CharField("Наполнитель",max_length=150)
    raskladniye = models.BooleanField("Раскладные")
    neraskladniye = models.BooleanField("Не раскладные")
    reclainer  = models.BooleanField("Реклайнеры")
    StilContour = models.BooleanField("Стиль Contour")
    StilHusk = models.BooleanField("Стиль Husk")
    VTkanini = models.BooleanField("В ткани")
    ObivPech = models.BooleanField("Обивка 'Пэчворк'")
    PovCresl = models.BooleanField("Поворотные кресла")
    kresla_krovati = models.BooleanField("Кресла-кровати")
    Novinki= models.BooleanField("Новинки")
    description = models.TextField("Описание", max_length=10000)
    def __str__(self):
        return self.title

class Crovati(models.Model):
    title = models.CharField("название ", max_length=150)
    price = models.IntegerField("цена")
    image = models.ImageField(upload_to='mebel/images/')
    image1 = models.ImageField(upload_to='mebel/images/')
    image2 = models.ImageField(upload_to='mebel/images/')
    image3 = models.ImageField(upload_to='mebel/images/')
    image4 = models.ImageField(upload_to='mebel/images/')
    image5 = models.ImageField(upload_to='mebel/images/')
    spal_mest = models.CharField("Спальное место:",max_length=200)
    width=models.CharField("Ширина",max_length=150)
    height_izg=models.CharField("Высота изголовья",max_length=150)
    height_izn=models.CharField("Высота изножья",max_length=150)
    dlina_width=models.CharField("Длина общая:",max_length=150)
    obivka =  models.CharField("Обивка",max_length=200)
    nojki =  models.CharField("Ножки",max_length=200)
    description = models.TextField("Описание",max_length=20000)
    podmeh= models.BooleanField("С подъемным механизмом")
    bezpodmeh= models.BooleanField("Без подъемного механизма")
    vtkanini= models.BooleanField("В ткани")
    Glyanez= models.BooleanField("Глянец")
    Novinki= models.BooleanField("Новинки")
    def __str__(self):
        return self.title
class Divani(models.Model):
    title = models.CharField("название ", max_length=150)
    price = models.IntegerField("цена")
    image = models.ImageField(upload_to='mebel/images/')
    image1 = models.ImageField(upload_to='mebel/images/')
    image2 = models.ImageField(upload_to='mebel/images/')
    image3 = models.ImageField(upload_to='mebel/images/')
    image4 = models.ImageField(upload_to='mebel/images/')
    image5 = models.ImageField(upload_to='mebel/images/')
    width=models.CharField("Ширина", max_length=150)
    deep=models.CharField("Глубина", max_length=150)
    deepSidBezPod=models.CharField("Глубина сиденья без подушек", max_length=150)
    height=models.CharField("Высота", max_length=150)
    heightPod=models.CharField("Высота подлокотника", max_length=150)
    heightSid=models.CharField("Высота сиденья", max_length=150)
    SleepMest=models.CharField("Спальное место",max_length=200)
    heightSpalMest=models.IntegerField("Высота спального места")
    TolshSpalMest=models.IntegerField("Толщина спального места")
    obivka =  models.CharField("Обивка",max_length=200)
    nojki =  models.CharField("Ножки",max_length=200)
    napolnitel = models.CharField("Наполнитель",max_length=160)
    mechanizm = models.CharField("Механизм",max_length=200)
    chehli = models.CharField("Чехлы",max_length=200)
    description = models.TextField("Описание",max_length=2000)
    threex=models.BooleanField("3x местные")
    two=models.BooleanField("2x местные")
    ugol=models.BooleanField("Угловые")
    rakladniye=models.BooleanField("Раскладные")
    nerakladniye=models.BooleanField("Не раскладные")
    raskpladVpered=models.BooleanField("Раскладывается вперёд")
    RasplaKaKnijka=models.BooleanField("Раскладывается как книжка")
    SDvuspalKrovat=models.BooleanField("С двуспальной кроватью")
    Novinki= models.BooleanField("Новинки")



    
    
    def __str__(self):
        return self.title
class Stoli(models.Model):
    title = models.CharField("название ", max_length=150)
    price = models.IntegerField("цена")
    image = models.ImageField(upload_to='mebel/images/')
    image1 = models.ImageField(upload_to='mebel/images/')
    image2 = models.ImageField(upload_to='mebel/images/')
    image3 = models.ImageField(upload_to='mebel/images/')
    image4 = models.ImageField(upload_to='mebel/images/')
    image5 = models.ImageField(upload_to='mebel/images/')
    height =  models.CharField("Высота",max_length=200)
    width =  models.CharField("Ширина",max_length=200)
    dlina =  models.CharField("Длина",max_length=200)
    diametr = models.CharField("Диаметр",max_length=200)
    stoleshnitsa = models.CharField("Столешница", max_length=150)
    nojki = models.CharField("Ножки", max_length=150)
    description=models.TextField("Описание", max_length=10000)
    raskladnoy = models.BooleanField("Раскладной")
    neraskladnoy = models.BooleanField("НеРаскладной")

    Stul_transformer = models.BooleanField("Стол-трансформер")
    Krug = models.BooleanField("Круглые столы")
    Oval = models.BooleanField("Овальные столы")
    PryamoUg = models.BooleanField("Прямоугольные столы")
    SoStecl = models.BooleanField("Со стеклом")
    SKeramPok = models.BooleanField("С керамическим покрытием")  
    JoutStoul = models.BooleanField("Журнальные столы")  
    Novinki= models.BooleanField("Новинки")   

    def __str__(self):
        return self.title


class Stulia(models.Model):
    title = models.CharField("название ", max_length=150)
    price = models.IntegerField("цена")

    image = models.ImageField(upload_to='mebel/images/')
    image1 = models.ImageField(upload_to='mebel/images/')
    image2 = models.ImageField(upload_to='mebel/images/')
    image3 = models.ImageField(upload_to='mebel/images/')
    image4 = models.ImageField(upload_to='mebel/images/')
    image5 = models.ImageField(upload_to='mebel/images/')
    width = models.CharField("Ширина",max_length=150)
    deep = models.CharField("Глубина",max_length=150)
    height_obj = models.CharField("Высотая общая",max_length=150)
    height_sid = models.CharField("Высота сиденья",max_length=150)
    obivka =  models.CharField("Обивка",max_length=200)
    nojki =  models.CharField("Ножки",max_length=200)
    description = models.TextField("Описание",max_length=20000)
    Plastic = models.BooleanField("Пластик")
    Tkanini = models.BooleanField("Ткань")
    EcoKoja = models.BooleanField("Эко кожа")
    ObivPecg = models.BooleanField("Обивка 'Пэчворк'")
    PovCresl = models.BooleanField("Поворотные кресла")
    DerevOsn = models.BooleanField("Деревянное основание")
    Novinki= models.BooleanField("Новинки")
    def __str__(self):
        return self.title    

class Fotki(models.Model):
    image = models.ImageField(upload_to='mebel/images/')




    