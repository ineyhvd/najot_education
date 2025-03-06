from django.db import models

class Talaba(models.Model):
    ism = models.CharField(max_length=100)
    familiya = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.ism} {self.familiya}"

class Davomat(models.Model):
    talaba = models.ForeignKey(Talaba, on_delete=models.CASCADE)
    sana = models.DateField()
    kelgan = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.talaba} - {self.sana}"

class Homework(models.Model):
    talaba = models.ForeignKey(Talaba, on_delete=models.CASCADE)  # O‘quvchi bilan bog‘lanish
    sana = models.DateField()  # Homework berilgan sana
    topshiriq = models.TextField()  # Homework matni
    bajarildi = models.BooleanField(default=False)  # Homework bajarildimi?

    def __str__(self):
        return f"{self.talaba} - {self.sana} - {self.topshiriq[:20]}..."