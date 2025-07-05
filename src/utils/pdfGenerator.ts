import jsPDF from 'jspdf';

interface PersonalInfo {
  fullName: string;
  email: string;
  phone: string;
  location: string;
  dateOfBirth: string;
  professionalSummary: string;
}

interface Experience {
  id: string;
  company: string;
  position: string;
  startDate: string;
  endDate: string;
  current: boolean;
  description: string;
}

interface Education {
  id: string;
  institution: string;
  degree: string;
  fieldOfStudy: string;
  startDate: string;
  endDate: string;
  gpa?: string;
}

interface CVData {
  personalInfo: PersonalInfo;
  experiences: Experience[];
  education: Education[];
  skills: string[];
  languages: string[];
  certifications: string[];
}

export const generatePDF = (cvData: CVData): void => {
  const doc = new jsPDF();
  let yPosition = 20;
  const pageWidth = doc.internal.pageSize.width;
  const margin = 20;
  const contentWidth = pageWidth - (margin * 2);

  // Helper function to add text with word wrapping
  const addText = (text: string, x: number, y: number, options: any = {}) => {
    const fontSize = options.fontSize || 10;
    const maxWidth = options.maxWidth || contentWidth;
    const lineHeight = options.lineHeight || fontSize * 0.4;
    
    doc.setFontSize(fontSize);
    if (options.style) {
      doc.setFont('helvetica', options.style);
    } else {
      doc.setFont('helvetica', 'normal');
    }
    
    const lines = doc.splitTextToSize(text, maxWidth);
    
    lines.forEach((line: string, index: number) => {
      doc.text(line, x, y + (index * lineHeight));
    });
    
    return y + (lines.length * lineHeight);
  };

  // Header - Name
  doc.setFillColor(59, 130, 246); // Blue color
  doc.rect(0, 0, pageWidth, 40, 'F');
  
  doc.setTextColor(255, 255, 255);
  yPosition = addText(cvData.personalInfo.fullName, margin, 25, {
    fontSize: 24,
    style: 'bold'
  });

  // Contact Information
  doc.setTextColor(255, 255, 255);
  const contactInfo = `${cvData.personalInfo.email} | ${cvData.personalInfo.phone} | ${cvData.personalInfo.location}`;
  yPosition = addText(contactInfo, margin, yPosition + 5, {
    fontSize: 10
  });

  // Reset text color for body
  doc.setTextColor(0, 0, 0);
  yPosition = 60;

  // Professional Summary
  if (cvData.personalInfo.professionalSummary) {
    yPosition = addText('PROFESSIONAL SUMMARY', margin, yPosition, {
      fontSize: 14,
      style: 'bold'
    });
    
    yPosition = addText(cvData.personalInfo.professionalSummary, margin, yPosition + 8, {
      fontSize: 10,
      lineHeight: 4
    });
    yPosition += 15;
  }

  // Experience
  if (cvData.experiences.length > 0) {
    yPosition = addText('PROFESSIONAL EXPERIENCE', margin, yPosition, {
      fontSize: 14,
      style: 'bold'
    });
    yPosition += 10;

    cvData.experiences.forEach((exp) => {
      // Check if we need a new page
      if (yPosition > 250) {
        doc.addPage();
        yPosition = 20;
      }

      // Job title
      yPosition = addText(exp.position, margin, yPosition, {
        fontSize: 12,
        style: 'bold'
      });

      // Company and dates
      const endDate = exp.current ? 'Present' : exp.endDate ? new Date(exp.endDate).toLocaleDateString('en-US', { month: 'long', year: 'numeric' }) : 'Present';
      const startDate = exp.startDate ? new Date(exp.startDate).toLocaleDateString('en-US', { month: 'long', year: 'numeric' }) : '';
      const companyInfo = `${exp.company} | ${startDate} - ${endDate}`;
      
      yPosition = addText(companyInfo, margin, yPosition + 5, {
        fontSize: 10,
        style: 'normal'
      });

      // Description
      if (exp.description) {
        const descriptions = exp.description.split('\n').filter(desc => desc.trim());
        descriptions.forEach(desc => {
          yPosition = addText(`• ${desc.trim()}`, margin, yPosition + 5, {
            fontSize: 9,
            lineHeight: 3.5
          });
        });
      }
      yPosition += 10;
    });
  }

  // Education
  if (cvData.education.length > 0) {
    // Check if we need a new page
    if (yPosition > 220) {
      doc.addPage();
      yPosition = 20;
    }

    yPosition = addText('EDUCATION', margin, yPosition, {
      fontSize: 14,
      style: 'bold'
    });
    yPosition += 10;

    cvData.education.forEach((edu) => {
      // Degree
      const degreeInfo = `${edu.degree} in ${edu.fieldOfStudy}`;
      yPosition = addText(degreeInfo, margin, yPosition, {
        fontSize: 12,
        style: 'bold'
      });

      // Institution and dates
      const endDate = edu.endDate ? new Date(edu.endDate).toLocaleDateString('en-US', { month: 'long', year: 'numeric' }) : 'Present';
      const startDate = edu.startDate ? new Date(edu.startDate).toLocaleDateString('en-US', { month: 'long', year: 'numeric' }) : '';
      let institutionInfo = `${edu.institution} | ${startDate} - ${endDate}`;
      if (edu.gpa) {
        institutionInfo += ` | GPA: ${edu.gpa}`;
      }
      
      yPosition = addText(institutionInfo, margin, yPosition + 5, {
        fontSize: 10
      });
      yPosition += 10;
    });
  }

  // Skills
  if (cvData.skills.length > 0) {
    // Check if we need a new page
    if (yPosition > 240) {
      doc.addPage();
      yPosition = 20;
    }

    yPosition = addText('SKILLS', margin, yPosition, {
      fontSize: 14,
      style: 'bold'
    });

    const skillsText = cvData.skills.filter(skill => skill.trim()).join(' • ');
    yPosition = addText(skillsText, margin, yPosition + 8, {
      fontSize: 10,
      lineHeight: 4
    });
    yPosition += 15;
  }

  // Languages
  if (cvData.languages.length > 0) {
    yPosition = addText('LANGUAGES', margin, yPosition, {
      fontSize: 14,
      style: 'bold'
    });

    const languagesText = cvData.languages.filter(lang => lang.trim()).join(' • ');
    yPosition = addText(languagesText, margin, yPosition + 8, {
      fontSize: 10,
      lineHeight: 4
    });
    yPosition += 15;
  }

  // Certifications
  if (cvData.certifications.length > 0) {
    yPosition = addText('CERTIFICATIONS', margin, yPosition, {
      fontSize: 14,
      style: 'bold'
    });
    yPosition += 8;

    cvData.certifications.filter(cert => cert.trim()).forEach((cert) => {
      yPosition = addText(`• ${cert}`, margin, yPosition, {
        fontSize: 10
      });
      yPosition += 5;
    });
  }

  // Save the PDF
  doc.save(`${cvData.personalInfo.fullName}_CV.pdf`);
};