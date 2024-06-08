from django.db import models

class IE(models.Model):
    organization_objective = models.TextField()
    leading_indicator = models.TextField()
    user_outcomes = models.TextField()
    model_properties = models.TextField()
    tanggal_mulai = models.DateField()
    tanggal_selesai = models.DateTimeField()
    status_penyelesaian = models.TextField()

class IntExp(models.Model):
    automate = models.TextField()
    prompt = models.TextField()
    organization = models.TextField()
    annotate = models.TextField()
    achieve_system = models.TextField()
    minimize_flaws = models.TextField()
    data_grown_system = models.TextField()

class IntImp(models.Model):
    proses_bisnis = models.TextField()
    teknologi_dipakai = models.TextField()
    sistem_cerdas = models.TextField()

class Kendala(models.Model) :
    masalah_pengembangan = models.TextField() 

class Status(models.Model) :
    status = models.TextField() 

class PerImp(models.Model) :
    pelaksanaan_deployment = models.TextField()
    pemeliharaan_sistem = models.TextField()
    pelaksanaan_operasi = models.TextField()
