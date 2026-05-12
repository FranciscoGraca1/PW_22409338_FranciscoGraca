from django.db import models

class Docente(models.Model):
    nome = models.CharField(max_length=100)
    biografia = models.TextField(blank=True)
    imagem = models.ImageField(upload_to='docentes/', blank=True)
    link_lusofona = models.URLField(blank=True)

    def __str__(self):
        return self.nome


class Licenciatura(models.Model):
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=10)
    instituicao = models.CharField(max_length=100)
    ano_inicio = models.IntegerField()
    descricao = models.TextField()
    link = models.URLField()

    def __str__(self):
        return self.nome

class UnidadeCurricular(models.Model):
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=20)
    ano = models.IntegerField()
    semestre = models.IntegerField()
    ects = models.IntegerField()
    descricao = models.TextField(blank=True)
    licenciatura = models.ForeignKey(Licenciatura, on_delete=models.CASCADE, related_name='ucs')
    docentes = models.ManyToManyField(Docente, related_name='ucs') # Relação correta

    def __str__(self):
        return self.nome

class TipoTecnologia(models.Model):
    nome = models.CharField(max_length=50) # Frontend, Backend, etc.
    def __str__(self): return self.nome

class Tecnologia(models.Model):
    nome = models.CharField(max_length=50)
    acronimo = models.CharField(max_length=10, blank=True)
    logo = models.ImageField(upload_to='tecnologias/', blank=True)
    link_oficial = models.URLField(blank=True)
    preferencia = models.IntegerField(default=1)
    descricao = models.TextField(blank=True) # Requisito 2.4.3
    tipo = models.ForeignKey(TipoTecnologia, on_delete=models.CASCADE, related_name='tecnologias', null=True) # Requisito 2.4.3

    def __str__(self): return self.nome

class Projeto(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='projetos/', blank=True)
    ano = models.IntegerField()
    github_link = models.URLField(blank=True)
    tecnologias = models.ManyToManyField(Tecnologia, related_name='projetos')
    uc = models.ForeignKey(UnidadeCurricular, on_delete=models.SET_NULL, null=True, blank=True, related_name='projetos')

    def __str__(self):
        return self.titulo

class TFC(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    ano = models.IntegerField()
    resumo = models.TextField()
    link_relatorio = models.URLField(blank=True)

    def __str__(self):
        return self.titulo
    
class Competencia(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    def __str__(self): return self.nome

class Formacao(models.Model):
    titulo = models.CharField(max_length=100)
    instituicao = models.CharField(max_length=100)
    ano = models.IntegerField()
    def __str__(self): return self.titulo