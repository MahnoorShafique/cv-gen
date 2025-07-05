from django.db import models
from django.contrib.auth.models import User

class CVProfile(models.Model):
    # Personal Information
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=255)
    date_of_birth = models.DateField(null=True, blank=True)
    professional_summary = models.TextField()
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"CV Profile - {self.full_name}"

class Experience(models.Model):
    cv_profile = models.ForeignKey(CVProfile, on_delete=models.CASCADE, related_name='experiences')
    company = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    current = models.BooleanField(default=False)
    description = models.TextField()
    
    class Meta:
        ordering = ['-start_date']
    
    def __str__(self):
        return f"{self.position} at {self.company}"

class Education(models.Model):
    cv_profile = models.ForeignKey(CVProfile, on_delete=models.CASCADE, related_name='education')
    institution = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    field_of_study = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    gpa = models.CharField(max_length=10, blank=True)
    
    class Meta:
        ordering = ['-end_date']
    
    def __str__(self):
        return f"{self.degree} in {self.field_of_study} from {self.institution}"

class Skill(models.Model):
    cv_profile = models.ForeignKey(CVProfile, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Language(models.Model):
    cv_profile = models.ForeignKey(CVProfile, on_delete=models.CASCADE, related_name='languages')
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Certification(models.Model):
    cv_profile = models.ForeignKey(CVProfile, on_delete=models.CASCADE, related_name='certifications')
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name