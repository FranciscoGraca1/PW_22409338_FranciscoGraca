from django.db import models

class Licenciatura(models.Model):
    nome = models.CharField(max_length=100)
    apresentacao = models.TextField()
    objetivos = models.TextField()
    duracao_anos = models.IntegerField()

    def __str__(self):
        return self.nome

class Docente(models.Model):
    nome = models.CharField(max_length=100)
    link_lusofona = models.URLField(blank=True)

    def __str__(self):
        return self.nome

class UnidadeCurricular(models.Model):
    nome = models.CharField(max_length=100)
    ano = models.IntegerField()
    semestre = models.IntegerField()
    ects = models.IntegerField()
    imagem = models.ImageField(upload_to='ucs/', blank=True)
    licenciatura = models.ForeignKey(Licenciatura, on_delete=models.CASCADE, related_name='ucs')
    docentes = models.ManyToManyField(Docente, related_name='ucs')

    def __str__(self):
        return self.nome

class Tecnologia(models.Model):
    nome = models.CharField(max_length=50)
    acronimo = models.CharField(max_length=10, blank=True)
    logo = models.ImageField(upload_to='tecnologias/', blank=True)
    link_oficial = models.URLField(blank=True)
    preferencia = models.IntegerField(default=1)

    def __str__(self):
        return self.nome

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