from django.contrib import admin

from .models import Despesa


class AdminDespesa(admin.ModelAdmin):
    list_display = ['data_criaçao','tipo_despesa','descriçao','forma_pagamento','vencimento','quitado','Dias_para_vencimento']
    list_filter = ['quitado','vencimento']

admin.site.register(Despesa,AdminDespesa)
