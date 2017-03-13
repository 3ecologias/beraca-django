# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from ckeditor.fields import RichTextField

class Fullwidth_slider_item(models.Model):
    first_phrase = models.CharField("Primeira frase (menor)", max_length=50, blank=False)
    second_phrase = models.CharField("Segunda frase (em destaque)", max_length=50, blank=False)
    slide_image = models.ImageField("Imagem do slide", upload_to='slide_item/%Y/%m/%d/', blank=False)

    def __unicode__(self):
        return self.first_phrase+" "+self.second_phrase

    class Meta:
        verbose_name = "Slide"
        verbose_name_plural = "Slides"

def generate_filename_miniature(self, filename):
    url = "Cases/miniaturas/%s/%s" % (self.title, filename)
    return url

class PortfolioItem(models.Model):
    #common

    title = models.CharField("Título", max_length=300, blank=False)
    sub_title = models.CharField("Subtítulo", max_length=300, blank=False)

    study = models.TextField('Estudo do caso', blank=True)
    results = models.TextField("Resultado", blank=True)
    experience = models.TextField("Experiência", blank=True)

    client = models.CharField("Cliente", max_length=300, blank=False)
    date = models.DateField(auto_now=True)
    online = models.CharField("URL do cliente", max_length=500, blank=True)

    #miniature
    miniature = models.ImageField("Miniatura", upload_to=generate_filename_miniature, blank=False)
    tag = models.CharField("Tag para filtro", max_length=300, blank=False)
    lat = models.CharField("Latitude", max_length=100, blank=True)
    lon = models.CharField("Longitude", max_length=100, blank=True)

    def __unicode__(self):
        return self.title

    def get_next(self):
        next = PortfolioItem.objects.filter(id__gt=self.id)
        if next:
          return next.first()
        return False

    def get_prev(self):
        prev = PortfolioItem.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
          return prev.first()
        return False

    class Meta:
        verbose_name="Portfolio/case"
        verbose_name_plural="Cases"
        ordering = ['-date']

def generate_filename(self, filename):
    url = "Portfolio/%s/%s" % (self.portfolio.title, filename)
    return url

class PortfolioImages(models.Model):
    portfolio = models.ForeignKey(PortfolioItem, related_name='images')
    image = models.ImageField("Primeira imagem(slide)", upload_to=generate_filename)

    def __unicode__(self):
        return self.portfolio.title

def generate_filename_miniature(self, filename):
    url = "Posts/miniaturas/%s/%s" % (self.title, filename)
    return url

class BlogPost(models.Model):
    #common

    title = models.CharField("Título", max_length=300, blank=False)
    sub_title = models.CharField("Sub-título", max_length=300, blank=False, null=True)
    intro = models.TextField("Introdução", blank=False)
    content = RichTextField("Corpo do texto", blank=False)
    date = models.DateField(auto_now=True)
    author = models.CharField("Autor", max_length=500, blank=True)

    #miniature
    miniature = models.ImageField("Miniatura", upload_to=generate_filename_miniature, blank=False)
    tag = models.CharField("Tag para filtro", max_length=300, blank=False)

    def __unicode__(self):
        return self.title

    def get_next(self):
        next = BlogPost.objects.filter(id__gt=self.id)
        if next:
          return next.first()
        return False

    def get_prev(self):
        prev = BlogPost.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
          return prev.first()
        return False

    class Meta:
        verbose_name="Blog post"
        verbose_name_plural="Posts"
        ordering = ['-date']

def generate_filename(self, filename):
    url = "Posts/%s/%s" % (self.post.title, filename)
    return url

class BlogImages(models.Model):
    post = models.ForeignKey(BlogPost, related_name='images')
    image = models.ImageField("Imagem", upload_to=generate_filename)

    def __unicode__(self):
        return self.post.title

def generate_filename(self, filename):
    url = "Service/%s/%s" % (self.title, filename)
    return url

class ServiceItem(models.Model):
    #common
    anchor = models.CharField("Âncora/Tab", max_length=300, blank=False)
    icon = models.ImageField("Ícone", upload_to=generate_filename)
    title = models.CharField("Título", max_length=300, blank=False)
    mention = models.TextField('Citação', blank=True)
    author = models.CharField("Autor", max_length=300, blank=False)
    abstract = models.TextField("Conceito", blank=True)
    conclusion = models.TextField("Conclusão", blank=True)
    description = models.TextField("Descrição", blank=True)
    date = models.DateField(auto_now=True)

    def __unicode__(self):
        return self.title

    def get_next(self):
        next = ServiceItem.objects.filter(id__gt=self.id)
        if next:
          return next.first()
        return False

    def get_prev(self):
        prev = ServiceItem.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
          return prev.first()
        return False

    class Meta:
        verbose_name="Service/case"
        verbose_name_plural="Services"
        ordering = ['-date']


class ServiceIcons(models.Model):
    service = models.ForeignKey(ServiceItem, related_name='icones')
    icon = models.ImageField("Ícone", upload_to=generate_filename, blank=True)
    title = models.CharField("Título", max_length=300, blank=True)

    def __unicode__(self):
        return self.service.title

class ServiceMethod(models.Model):
    method = models.ForeignKey(ServiceItem, related_name='methods')
    image = models.ImageField("Imagem", upload_to=generate_filename, blank=True)
    title = models.CharField("Título", max_length=300, blank=True)
    desc = models.TextField("Descrição", max_length=300, blank=True)

    def __unicode__(self):
        return self.method.title
