from django.db import models

# created_at - дата создания

class Article(models.Model):
    # id - джанго создает автоматически
    # по умолчанию все поля обязательно должны быть заполнены
    title = models.CharField(max_length=255) # название статьи включает максимут 255 символов
    content = models.TextField(blank=True) # большой массив текста, blank=True - поле можно не заполнять
    created_at = models.DateTimeField(auto_now_add=True) # дата создания, auto_now_add = True - зап. автомат. при создании
    updated_at = models.DateTimeField(auto_now=True) # дата изменения, auto_now = True - запис. дата редактирования (при каждом сохранении устанавливается текущая дата)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/') #изображение, механизм загрузки изображения встроен в библиотеку Pillow
                              # upload_to - куда загружать изображения
                              # 'photos/%Y/%m/%d' - изображения будут загружаться в папку 'photos' и распределяться по подпапкам год/месяц/день