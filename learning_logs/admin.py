from django.contrib import admin

from learning_logs.models import Topic, Entry


class EntryAdmin(admin.ModelAdmin):
    '''
    Изменение статуса записи.

    '''

    list_display   = ['topic', 'text', 'entry_status', 'verified_adm']
    ordering       = ['text',]
    actions        = ['verificate_entry', 'reject_entry']
    date_hierarchy = 'date_added'
    list_filter    = ['topic', 'entry_status', 'verified_adm', 'date_added']

    def verificate_entry(self, request, queryset):
        '''
        Обновляет статус записи на "Проверено" со стороны администратора,
         далее запись будет опубликована на главной странице.

        '''

        queryset.update(verified_adm='ok')

    verificate_entry.short_description = 'To verificate, publish entry'

    def reject_entry(self, request, queryset):
        '''
        Обновляет статус записи на "Отклонено" со стороны администратора,
         запись не будет опубликована на главной странице..

        '''

        queryset.update(verified_adm='no')

    reject_entry.short_description = 'To reject entry'


'''class ForVerificationAdmin(admin.ModelAdmin):
    #


    list_display   = ['text']
    ordering       = ['text',]
    #actions        = ['verificate_entry', 'reject_entry']
    #date_hierarchy = 'date_added'
    #list_filter    = ['verification', 'status']'''

   

admin.site.register(Topic)
admin.site.register(Entry, EntryAdmin)
#admin.site.register(ForVerification)