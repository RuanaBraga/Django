from django.db import models

tupla =(('Roupas','Roupas'),('Remedio','Remédio'),('Alimentaçao','Alimentaçao'),('Educaçao','Eduçação'),('Transporte','Transporte'),('Outros','Outros'))
tupla_Pagamento = (('Dinherio','Dinheiro'),('Cartao de Credito','Cartao de Credito'),('Cartao Debito','Cartao Debito'),
     ('Cartao Crediario','Cartao Crediario'),('Cheque','Cheque'))




class Despesa(models.Model):
    data_criaçao = models.DateField()
    tipo_despesa = models.CharField(max_length=1000,choices= tupla)
    descriçao = models.CharField(max_length=200)
    forma_pagamento = models.CharField(max_length=1000,choices=tupla_Pagamento)
    vencimento = models.DateField()
    quitado = models.BooleanField()

    def Dias_para_vencimento(self):
        return (self.vencimento - self.data_criaçao).days

    def __str__(self):
        return self.tipo_despesa





