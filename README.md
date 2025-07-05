# CVCraft - Professional CV Generator

A modern, professional CV generator built with React and Django, containerized with Docker for easy deployment.

## Features

- **Beautiful UI**: Clean, modern interface with step-by-step form wizard
- **Professional Templates**: AI-powered CV generation with professional formatting
- **Full-Stack Solution**: React frontend with Django REST API backend
- **PDF Generation**: High-quality PDF output with professional styling
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile
- **Dockerized**: Easy deployment with Docker and Docker Compose
- **Production Ready**: Scalable architecture with proper separation of concerns

## Tech Stack

### Frontend
- React 18 with TypeScript
- Tailwind CSS for styling
- Lucide React for icons
- Vite for build tooling

### Backend
- Django 4.2 with Django REST Framework
- ReportLab for PDF generation
- SQLite database (easily replaceable with PostgreSQL)
- CORS support for frontend integration

### DevOps
- Docker & Docker Compose
- Environment-based configuration
- Production-ready containerization

## Quick Start

### Prerequisites
- Docker and Docker Compose installed
- Node.js 18+ (for local development)
- Python 3.11+ (for local development)

### Run with Docker (Recommended)

1. Clone the repository:
```bash
git clone <repository-url>
cd cvcraft
```

2. Build and run with Docker Compose:
```bash
docker-compose up --build
```

3. Open your browser:
- Frontend: http://localhost:5173
- Backend API: http://localhost:8000

### Local Development

#### Frontend Setup
```bash
# Install dependencies
npm install

# Start development server
npm run dev
```

#### Backend Setup
```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start development server
python manage.py runserver
```

## Project Structure

```
cvcraft/
├── src/                    # React frontend
│   ├── components/         # React components
│   ├── App.tsx            # Main app component
│   └── main.tsx           # App entry point
├── backend/               # Django backend
│   ├── cvgenerator/       # Django project settings
│   ├── cvapp/             # Main Django app
│   ├── requirements.txt   # Python dependencies
│   └── manage.py          # Django management script
├── docker-compose.yml     # Docker Compose configuration
├── Dockerfile.frontend    # Frontend Docker configuration
└── README.md             # This file
```

## API Endpoints

- `POST /api/generate-cv/` - Generate CV PDF from form data
- `GET /api/health/` - Health check endpoint

## Features in Detail

### Multi-Step Form
- Personal Information
- Professional Experience
- Education History
- Skills, Languages, and Certifications

### Professional CV Generation
- Clean, modern template design
- Proper typography and spacing
- Professional color scheme
- ATS-friendly formatting

### Responsive Design
- Mobile-first approach
- Optimized for all screen sizes
- Touch-friendly interface

## Environment Variables

### Backend (.env)
```
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

## Deployment

### Docker Deployment
The application is fully containerized and ready for deployment on any platform that supports Docker:

- AWS ECS/Fargate
- Google Cloud Run
- Azure Container Instances
- DigitalOcean App Platform
- Heroku
- Any VPS with Docker

### Production Considerations
- Set `DEBUG=False` in production
- Use a production database (PostgreSQL recommended)
- Configure proper CORS settings
- Set up proper logging
- Use environment-specific settings

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License.