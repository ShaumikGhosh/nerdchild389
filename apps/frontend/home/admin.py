from django.contrib import admin
from .models import *


@admin.register(PetInfo)
class HomeAdmin(admin.ModelAdmin):

    list_display = ('pet_name', 'pet_breed', 'age', 'weight', 'unique_id', 'created_at')
    list_per_page = 10
    search_fields = ('uni_pk',)

    def age(self, obj):
        return f"{obj.pet_age} Years old"

    def weight(self, obj):
        return f"{obj.pet_weight} KG"

    def unique_id(self, obj):
        return obj.uni_pk
    unique_id.short_description = "Unique Pet ID"


@admin.register(PetSymptom)
class HomeAdmin(admin.ModelAdmin):

    list_display = ('symptom', 'solution', 'author', 'created_at')
    list_per_page = 10
    search_fields = ('pet__uni_pk',)

    def symptom(self, obj):
        if obj.symptom_type == "pn":
            return "Pain"
        if obj.symptom_type == "ca":
            return "Chronic Anxiety"
        if obj.symptom_type == "is":
            return "Itching/Scratching"

    def solution(self, obj):
        if obj.symptom_type == "pn":
            return "Stress Reliever"
        if obj.symptom_type == "ca":
            return "Veterinarian Consult"
        if obj.symptom_type == "is":
            return "Stress Reliever, Veterinarian Consult"

    def author(self, obj):
        return obj.pet.uni_pk
    author.short_description = "Unique Pet ID"
