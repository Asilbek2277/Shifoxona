from django.db import models

class Xona(models.Model):
    number=models.IntegerField()
    band=models.BooleanField()
    joy=models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.number}"

class Xizmat(models.Model):
    nom=models.CharField(max_length=30)
    xona=models.ForeignKey(Xona, on_delete=models.CASCADE)
    narx=models.CharField(max_length=20)

    def __str__(self):
        return self.nom



class Shifokor(models.Model):
    ism=models.CharField(max_length=50)
    ish_vaqti=models.CharField(max_length=40)
    tel=models.CharField(max_length=20)
    xizmat=models.ForeignKey(Xizmat, on_delete=models.CASCADE)

    def __str__(self):
        return self.Ism_familiya

class Buyurtma(models.Model):
    sana=models.DateField()
    tashhis=models.TextField()
    xona=models.ForeignKey(Xona, on_delete=models.CASCADE)
    shifokor=models.ForeignKey(Shifokor, on_delete=models.CASCADE)
    kishi_soni=models.PositiveSmallIntegerField()
    summa=models.FloatField()
    tuzaldi=models.BooleanField(default=False)
    def __str__(self):
        return self.Tashhis


class Bemor(models.Model):
    ism=models.CharField(max_length=50)
    tel=models.CharField(max_length=20)
    buyurtma=models.ForeignKey(Buyurtma, on_delete=models.CASCADE)

    def __str__(self):
        return self.Ism_familiya
