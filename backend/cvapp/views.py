from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from .models import CVProfile, Experience, Education, Skill, Language, Certification
from .cv_generator import generate_cv_pdf
import json

@api_view(['POST'])
def generate_cv(request):
    try:
        data = request.data
        
        # Create CV Profile
        cv_profile = CVProfile.objects.create(
            full_name=data['personalInfo']['fullName'],
            email=data['personalInfo']['email'],
            phone=data['personalInfo']['phone'],
            location=data['personalInfo']['location'],
            date_of_birth=data['personalInfo']['dateOfBirth'] if data['personalInfo']['dateOfBirth'] else None,
            professional_summary=data['personalInfo']['professionalSummary']
        )
        
        # Create Experiences
        for exp_data in data['experiences']:
            Experience.objects.create(
                cv_profile=cv_profile,
                company=exp_data['company'],
                position=exp_data['position'],
                start_date=exp_data['startDate'],
                end_date=exp_data['endDate'] if exp_data['endDate'] else None,
                current=exp_data['current'],
                description=exp_data['description']
            )
        
        # Create Education
        for edu_data in data['education']:
            Education.objects.create(
                cv_profile=cv_profile,
                institution=edu_data['institution'],
                degree=edu_data['degree'],
                field_of_study=edu_data['fieldOfStudy'],
                start_date=edu_data['startDate'],
                end_date=edu_data['endDate'],
                gpa=edu_data.get('gpa', '')
            )
        
        # Create Skills
        for skill_name in data['skills']:
            if skill_name.strip():
                Skill.objects.create(cv_profile=cv_profile, name=skill_name)
        
        # Create Languages
        for lang_name in data['languages']:
            if lang_name.strip():
                Language.objects.create(cv_profile=cv_profile, name=lang_name)
        
        # Create Certifications
        for cert_name in data['certifications']:
            if cert_name.strip():
                Certification.objects.create(cv_profile=cv_profile, name=cert_name)
        
        # Generate PDF
        pdf_buffer = generate_cv_pdf(cv_profile)
        
        # Return PDF as response
        response = HttpResponse(pdf_buffer, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{cv_profile.full_name}_CV.pdf"'
        return response
        
    except Exception as e:
        return Response(
            {'error': f'Error generating CV: {str(e)}'}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@api_view(['GET'])
def health_check(request):
    return Response({'status': 'healthy'}, status=status.HTTP_200_OK)