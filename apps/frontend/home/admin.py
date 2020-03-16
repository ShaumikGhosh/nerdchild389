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

    list_display = ('symptom', 'author', 'created_at')
    list_per_page = 10
    search_fields = ('pet__uni_pk',)

    def symptom(self, obj):
        if obj.symptom_type == "pn":
            return "Pain"

    def author(self, obj):
        return obj.pet.uni_pk
    author.short_description = "Unique Pet ID"


@admin.register(EmailFromVisitor)
class VisitorEmail(admin.ModelAdmin):

    list_display = ('email', 'subject', 'username', 'message', 'related_pet', 'created_at')
    search_fields = ('user__uni_pk',)
    list_per_page = 10

    def email(self, obj):
        return obj.v_email
    email.short_description ="User Email"

    def subject(self, obj):
        return obj.v_subject
    subject.short_description ="Sender Subject"

    def username(self, obj):
        return obj.v_user_name
    username.short_description ="Sender Name"

    def message(self, obj):
        return obj.v_message
    message.short_description ="Sender Message"

    def related_pet(self, obj):
        return obj.user.uni_pk
    related_pet.short_description ="His/Her Pet ID"


@admin.register(Product)
class Product(admin.ModelAdmin):
    pass
