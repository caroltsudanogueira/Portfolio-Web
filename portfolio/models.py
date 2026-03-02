from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self): return self.nome

class Projeto(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='projetos/')
    tecnologias = models.CharField(max_length=200) # O "Info" do seu DER
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    github_link = models.URLField(blank=True)

class Contato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    mensagem = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} - {self.email}"