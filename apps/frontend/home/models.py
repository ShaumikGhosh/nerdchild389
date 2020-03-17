from django.db import models


class CommonModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class PetInfo(CommonModel):

    pet_name = models.CharField(max_length=100, null=False, blank=False)
    pet_breed = models.CharField(max_length=100, null=False, blank=False)
    pet_age = models.IntegerField(null=False, blank=False)
    pet_weight = models.IntegerField(null=False, blank=False)
    uni_pk = models.TextField(null=False, blank=False, unique=True)

    class Meta:
        db_table = 'PetInfo'


class PetSymptom(CommonModel):

    symptom_type = models.CharField(max_length=100, null=False, blank=False)
    pet = models.ForeignKey(PetInfo, on_delete=models.CASCADE, null=False, blank=False)

    class Meta:
        db_table = 'PetSymptom'
