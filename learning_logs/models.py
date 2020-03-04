from django.db                  import models
from django.contrib.auth.models import User


# Create your models here.
class Topic(models.Model):
    '''
    Тема, которую изучает пользователь.

    '''
    
    text       = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner      = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        '''
        Возвращает строковое представление модели.

        '''

        return self.text


class Entry(models.Model):
    '''
    Информация, изученная пользователем по теме.

    '''

    STATUS_CHOICES = [
            ('pr', 'Private'),
            ('pb', 'Published'),
    ]

    VERIF_STATUS = [
        ('ok', 'Verified'),
        ('no', 'Reject'),
    ]

    topic        = models.ForeignKey(Topic, on_delete=models.PROTECT)
    text         = models.TextField()
    date_added   = models.DateTimeField(auto_now_add=True)    
    entry_status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='')
    verified_adm = models.CharField(max_length=2, choices=VERIF_STATUS, default='')
    tag          = models.CharField(max_length=100, default='')


    class Meta:
        verbose_name_plural = 'entries'


    def __str__(self):
        '''
        Возвращает строковое представление модели.

        '''

        if len(self.text) >= 50:
            return self.text[:50] + '...'

        else:
            return self.text[:50]


'''class ForVerification(Entry):
    
    #Модель, наследуемая от Entry, чтобы отобразить 
     #записи на сайте администратора в отдельной графе.

    

    status       = Entry.objects.filter(entry_status='pb')'''
