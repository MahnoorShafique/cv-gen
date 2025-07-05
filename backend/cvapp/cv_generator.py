from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import Color, black, white
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.pdfgen import canvas
from io import BytesIO
import re

def generate_cv_pdf(cv_profile):
    """Generate a professional CV PDF from CV profile data"""
    
    # Create PDF buffer
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=18)
    
    # Define colors
    primary_color = Color(0.23, 0.51, 0.96)  # Blue
    secondary_color = Color(0.4, 0.4, 0.4)  # Gray
    accent_color = Color(0.06, 0.72, 0.63)  # Teal
    
    # Create styles
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=28,
        spaceAfter=12,
        textColor=primary_color,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Normal'],
        fontSize=12,
        spaceAfter=20,
        textColor=secondary_color,
        alignment=TA_CENTER,
        fontName='Helvetica'
    )
    
    section_header_style = ParagraphStyle(
        'SectionHeader',
        parent=styles['Heading2'],
        fontSize=16,
        spaceAfter=12,
        spaceBefore=24,
        textColor=primary_color,
        fontName='Helvetica-Bold',
        borderWidth=1,
        borderColor=primary_color,
        borderPadding=6
    )
    
    normal_style = ParagraphStyle(
        'CustomNormal',
        parent=styles['Normal'],
        fontSize=10,
        spaceAfter=6,
        textColor=black,
        fontName='Helvetica'
    )
    
    job_title_style = ParagraphStyle(
        'JobTitle',
        parent=styles['Normal'],
        fontSize=12,
        spaceAfter=4,
        textColor=primary_color,
        fontName='Helvetica-Bold'
    )
    
    company_style = ParagraphStyle(
        'Company',
        parent=styles['Normal'],
        fontSize=11,
        spaceAfter=4,
        textColor=black,
        fontName='Helvetica-Bold'
    )
    
    date_style = ParagraphStyle(
        'Date',
        parent=styles['Normal'],
        fontSize=10,
        spaceAfter=8,
        textColor=secondary_color,
        fontName='Helvetica-Oblique'
    )
    
    # Build content
    content = []
    
    # Header - Name and Contact Info
    content.append(Paragraph(cv_profile.full_name, title_style))
    
    contact_info = f"{cv_profile.email} | {cv_profile.phone} | {cv_profile.location}"
    content.append(Paragraph(contact_info, subtitle_style))
    
    # Professional Summary
    if cv_profile.professional_summary:
        content.append(Paragraph("PROFESSIONAL SUMMARY", section_header_style))
        content.append(Paragraph(cv_profile.professional_summary, normal_style))
    
    # Experience
    experiences = cv_profile.experiences.all()
    if experiences:
        content.append(Paragraph("PROFESSIONAL EXPERIENCE", section_header_style))
        
        for exp in experiences:
            # Job title
            content.append(Paragraph(exp.position, job_title_style))
            
            # Company and dates
            end_date = "Present" if exp.current else exp.end_date.strftime("%B %Y") if exp.end_date else "Present"
            start_date = exp.start_date.strftime("%B %Y")
            company_info = f"{exp.company} | {start_date} - {end_date}"
            content.append(Paragraph(company_info, company_style))
            
            # Description
            if exp.description:
                # Split description into bullet points if it contains line breaks
                descriptions = exp.description.split('\n')
                for desc in descriptions:
                    if desc.strip():
                        content.append(Paragraph(f"• {desc.strip()}", normal_style))
            
            content.append(Spacer(1, 12))
    
    # Education
    education = cv_profile.education.all()
    if education:
        content.append(Paragraph("EDUCATION", section_header_style))
        
        for edu in education:
            # Degree
            degree_info = f"{edu.degree} in {edu.field_of_study}"
            content.append(Paragraph(degree_info, job_title_style))
            
            # Institution and dates
            end_date = edu.end_date.strftime("%B %Y") if edu.end_date else "Present"
            start_date = edu.start_date.strftime("%B %Y")
            institution_info = f"{edu.institution} | {start_date} - {end_date}"
            if edu.gpa:
                institution_info += f" | GPA: {edu.gpa}"
            content.append(Paragraph(institution_info, company_style))
            
            content.append(Spacer(1, 12))
    
    # Skills
    skills = cv_profile.skills.all()
    if skills:
        content.append(Paragraph("SKILLS", section_header_style))
        skill_names = [skill.name for skill in skills]
        skills_text = " • ".join(skill_names)
        content.append(Paragraph(skills_text, normal_style))
    
    # Languages
    languages = cv_profile.languages.all()
    if languages:
        content.append(Paragraph("LANGUAGES", section_header_style))
        language_names = [lang.name for lang in languages]
        languages_text = " • ".join(language_names)
        content.append(Paragraph(languages_text, normal_style))
    
    # Certifications
    certifications = cv_profile.certifications.all()
    if certifications:
        content.append(Paragraph("CERTIFICATIONS", section_header_style))
        for cert in certifications:
            content.append(Paragraph(f"• {cert.name}", normal_style))
    
    # Build PDF
    doc.build(content)
    
    # Get PDF data
    pdf_data = buffer.getvalue()
    buffer.close()
    
    return pdf_data