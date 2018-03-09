# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField


class Categorie(models.Model):
    nom = models.CharField(max_length=200, unique=True)

    class Meta:
       ordering = ['nom']

    def __str__(self):
        return '%s' % self.nom

    def __unicode__(self):
        return u'%s' % self.nom

class Oeuvre(models.Model):
    titre = models.CharField(verbose_name="Titre de l'oeuvre s'il y en a un", max_length=250, blank=True, null=True, )
    ordre = models.IntegerField(verbose_name="Ordre dans sa categorie (optionnel)", blank=True, null=True, )
    texte = RichTextField(verbose_name="Description ou commentaires sur l'oeuvre",config_name='billet', blank=True, null=True, )
    periode = models.CharField(verbose_name="Année ou période", max_length=250, blank=True, null=True, )
    categorie = models.ForeignKey(Categorie, verbose_name="Type d'oeuvre (va être utilisé pour déterminer l'affichage)", on_delete=models.DO_NOTHING)
    dimension = models.CharField(verbose_name="Dimensions", max_length=250, blank=True, null=True, )
    photo = models.ImageField(upload_to="images", verbose_name="Pour les fichiers d'images", blank=True, null=True)
    livret = models.FileField(upload_to='RC', verbose_name="Pour les pdf", blank=True, null=True)

    class Meta:
       ordering = ['titre', ]

    def __str__(self):
        return '%s' % self.titre

    def __unicode__(self):
        return u'%s' % self.titre

