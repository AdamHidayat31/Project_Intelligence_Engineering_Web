from django.db import models

class DataProjek(models.Model):
    nama_proyek = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.nama_proyek

class IE(models.Model):
    projek = models.OneToOneField(DataProjek, on_delete=models.CASCADE, null=True)
    organization_objective = models.TextField(null=True)
    leading_indicator = models.TextField(null=True)
    user_outcomes = models.TextField(null=True)
    model_properties = models.TextField(null=True)
    tanggal_mulai = models.DateField()
    tanggal_selesai = models.DateTimeField()
    status_penyelesaian = models.TextField()

class IntExp(models.Model):
    projek = models.ForeignKey(DataProjek, on_delete=models.CASCADE, null=True)
    automate = models.TextField(null=True)
    prompt = models.TextField(null=True)
    organization = models.TextField(null=True)
    annotate = models.TextField(null=True)
    achieve_system = models.TextField()
    minimize_flaws = models.TextField()
    data_grown_system = models.TextField()

class IntImp(models.Model):
    projek = models.ForeignKey(DataProjek, on_delete=models.CASCADE, null=True)
    proses_bisnis = models.TextField()
    teknologi_dipakai = models.TextField()
    sistem_cerdas = models.TextField()

class Kendala(models.Model):
    projek = models.ForeignKey(DataProjek, on_delete=models.CASCADE, null=True)
    masalah_pengembangan = models.TextField()

class Status(models.Model):
    projek = models.ForeignKey(DataProjek, on_delete=models.CASCADE, null=True)
    status = models.TextField()

class PerImp(models.Model):
    projek = models.ForeignKey(DataProjek, on_delete=models.CASCADE, null=True)
    pelaksanaan_deployment = models.TextField()
    pemeliharaan_sistem = models.TextField()
    pelaksanaan_operasi = models.TextField()

class ProjectInfo(models.Model):
    nama_project = models.CharField(max_length=100)
    tujuan_project = models.CharField(max_length=1000)
    tangmul_project = models.DateField()
    tangsel_project = models.DateField()
    pic_project = models.CharField(max_length=40)
    status_project = models.TextField()
    biaya = models.DecimalField(max_digits=12, decimal_places=2, default=0.00, blank=True, null=True)
    projek = models.ForeignKey(DataProjek, on_delete=models.CASCADE, related_name='projects', null=True)


