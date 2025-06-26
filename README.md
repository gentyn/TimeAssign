# TimeAssign - Modern Course Management System

A modern, responsive Django web application for managing time assignments, courses, and user roles in academic settings. Built with Django 5.2.3 and featuring a beautiful, accessible UI with UWM branding.

## ✨ Features

### 🎯 Core Functionality
- **User Management**: Add, view, and manage users with role-based permissions
- **Course Management**: Create, edit, and organize courses with detailed scheduling
- **Role-Based Access Control**: Secure access for Chair, Instructor, and TA roles
- **Schedule Management**: Comprehensive scheduling system with conflict validation
- **Break Management**: Personal break scheduling for TAs
- **Assignment System**: Assign users to courses with validation

### 🎨 Modern UI/UX
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices
- **Dark/Light Mode**: Toggle between themes with system preference detection
- **UWM Branding**: Official University of Wisconsin-Milwaukee colors and styling
- **Accessibility**: WCAG compliant with proper ARIA labels and keyboard navigation
- **Modern Components**: Cards, buttons, forms, and navigation with hover effects
- **Personalized Experience**: Welcome messages with user names and roles

### 🔐 Authentication & Security
- **Dual Authentication**: Supports both Django's built-in auth and legacy system
- **Session Management**: Secure session handling with automatic redirects
- **Role-Based Permissions**: Granular access control based on user roles
- **CSRF Protection**: Built-in Django security features

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository:**
```bash
git clone <your-repo-url>
cd TimeAssign
```

2. **Create and activate virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Run database migrations:**
```bash
python manage.py migrate
```

5. **Start the development server:**
```bash
python manage.py runserver
```

6. **Access the application:**
   - Open your browser and navigate to `http://127.0.0.1:8000/`
   - For admin access: `http://127.0.0.1:8000/admin/`

## 🏗️ Project Structure

```
TimeAssign/
├── ta_app/                 # Main Django application
│   ├── models.py          # Database models
│   ├── views.py           # View logic and routing
│   ├── sitelogic/         # Business logic modules
│   └── tests/             # Test files
├── templates/             # HTML templates
│   ├── base.html          # Base template with navigation
│   └── main/              # Page-specific templates
├── static/                # Static files
│   ├── images/            # University logos and images
│   └── css/               # Custom stylesheets
├── timeassign/            # Django project settings
│   ├── settings.py        # Application settings
│   ├── urls.py            # URL routing
│   └── wsgi.py            # WSGI configuration
└── requirements.txt       # Python dependencies
```

## 🎨 Design System

### Color Palette
- **UWM Gold**: `#FFBD00` - Primary brand color
- **Silver Gray**: `#CCCCCC` - Secondary color
- **Black**: `#000000` - Text and accents
- **White**: `#FFFFFF` - Backgrounds

### Typography
- **Font Family**: System fonts with fallbacks
- **Logo**: Custom styled "TimeAssign" with drop shadows
- **Headings**: Bold, hierarchical typography
- **Body Text**: Readable, accessible font sizes

### Components
- **Cards**: Elevated containers with shadows and hover effects
- **Buttons**: Primary (gold) and secondary (gray) with hover states
- **Forms**: Modern input fields with focus states
- **Navigation**: Responsive navbar with theme toggle

## 👥 User Roles & Permissions

### Chair
- Full system access
- User management (add, view, edit users)
- Course management (add, view, edit courses)
- Assignment management (assign users to courses)
- Validation and conflict resolution

### Instructor
- Course assignment management
- TA assignment to courses
- Schedule validation
- Course overview access

### TA (Teaching Assistant)
- Personal schedule management
- Break scheduling and editing
- Course viewing access
- Schedule conflict validation

## 🔧 Technical Stack

- **Backend**: Django 5.2.3
- **Database**: SQLite (production-ready databases supported)
- **Frontend**: HTML5, CSS3, Tailwind CSS
- **JavaScript**: Vanilla JS for theme toggle and interactions
- **Authentication**: Django's built-in auth + custom legacy system
- **Deployment**: WSGI compatible (Gunicorn, uWSGI)

## 🌟 Recent Improvements

### UI/UX Enhancements
- ✅ Complete visual redesign with modern styling
- ✅ Responsive layout for all screen sizes
- ✅ Dark/light mode toggle with system preference detection
- ✅ UWM branding and color scheme
- ✅ Improved typography and accessibility
- ✅ Enhanced navigation with smart routing

### User Experience
- ✅ Personalized welcome messages with user names
- ✅ Intelligent navigation (logo links to menu when logged in)
- ✅ Automatic redirects (no more "already logged in" dialogs)
- ✅ Improved form styling and validation feedback
- ✅ Better error handling and user feedback

### Technical Improvements
- ✅ Modern CSS with Tailwind framework
- ✅ Optimized session management
- ✅ Enhanced security with proper CSRF protection
- ✅ Improved code organization and maintainability
- ✅ Better responsive design implementation

## 🧪 Testing

Run the test suite:
```bash
python manage.py test
```

## 📝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Support

For support and questions:
- Create an issue in the repository
- Contact the development team
- Check the documentation in the `/docs` folder

---

**TimeAssign** - Modern Course Management System for Academic Excellence 