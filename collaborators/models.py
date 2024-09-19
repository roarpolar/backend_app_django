from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
import random

def validar_cpf(cpf: str) -> None:
    """
    Valida se o CPF tem exatamente 11 dígitos numéricos.
    """
    if not cpf.isdigit() or len(cpf) != 11:
        raise ValidationError('O CPF deve conter exatamente 11 dígitos numéricos.')

# Modelo Colaborador
class Colaborador(models.Model):
    imagem = models.ImageField(upload_to="icones", null=True, blank=True)  # Foto é opcional
    nome = models.CharField(max_length=30)
    cpf = models.CharField(max_length=14, unique=True, validators=[validar_cpf])  # CPF com validação
    data_nasc = models.DateField()  # Campo para a data de nascimento
    telefone_contato = models.CharField(max_length=15, blank=True, null=True)  # Telefone de contato
    email = models.EmailField(max_length=254, blank=True, null=True)  # E-mail
    funcao = models.CharField(max_length=50, blank=True, null=True)  # Função (profissão)
    add_matricula = models.CharField(max_length=5, unique=True, blank=True, null=True)  # Matrícula com até 5 dígitos
    senha = models.CharField(max_length=6, unique=True, blank=True, null=True)  # Senha de 6 dígitos não repetidos
    observacoes = models.TextField(max_length=2000, blank=True, null=True)  # Campo para observações

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        if not self.senha:
            self.senha = self.gerar_senha()
        super().save(*args, **kwargs)

    def gerar_senha(self):
        """Gera uma senha de 6 números únicos"""
        while True:
            senha = ''.join(random.sample('0123456789', 6))
            if not Colaborador.objects.filter(senha=senha).exists():
                return senha

