from django.db import models

# Create your models here.


class Post(models.Model):
    
    title = models.CharField(verbose_name='Título',max_length=100,unique=True)
    content = models.TextField(verbose_name='Conteudo')
    created_at = models.DateTimeField(verbose_name="Criado em",editable=False,auto_now_add=True, blank=True)
    tags = models.ManyToManyField('Tag',verbose_name='Tags')

#Dados: title, content, created_at, tags (um post tem uma ou várias tags e uma tag pode ter um ou vários posts)


class Tag(models.Model):
    name = models.CharField(verbose_name='Nome',max_length=100,unique=True)