from django.contrib import admin
from .models import CVProfile, Experience, Education, Skill, Language, Certification

@admin.register(CVProfile)
class CVProfileAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'phone', 'created_at']
    search_fields = ['full_name', 'email']
    list_filter = ['created_at', 'updated_at']

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['position', 'company', 'cv_profile', 'start_date', 'current']
    list_filter = ['current', 'start_date']
    search_fields = ['position', 'company', 'cv_profile__full_name']

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['degree', 'institution', 'cv_profile', 'end_date']
    list_filter = ['end_date']
    search_fields = ['degree', 'institution', 'cv_profile__full_name']

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'cv_profile']
    search_fields = ['name', 'cv_profile__full_name']

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['name', 'cv_profile']
    search_fields = ['name', 'cv_profile__full_name']

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ['name', 'cv_profile']
    search_fields = ['name', 'cv_profile__full_name']