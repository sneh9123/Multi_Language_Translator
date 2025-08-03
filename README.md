# 🌍 Multi-Language Course Content Translator

A Flask-based web application that translates educational content between multiple languages using AI-powered translation with IBM Cloud API integration.

## 📚 Overview

This application helps educators and students break down language barriers in education by providing accurate, context-aware translations of course materials. It supports various academic subjects and maintains educational terminology across different languages.

## ✨ Features

### 🎯 Core Functionality
- **Multi-language Translation**: Support for 8 languages (English, Hindi, Marathi, Tamil, Bengali, Telugu, Kannada, Gujarati)
- **Academic Subject Support**: Specialized translation for Mathematics, Science, History, Geography, Literature, Computer Science, Economics, Political Science, Biology, Chemistry, Physics
- **Content Type Support**: Lecture Notes, Presentation Slides, Textbook Chapters, Assignments, Exam Papers, Study Guides, Research Papers
- **Academic Level Adaptation**: Primary School, Secondary School, Higher Secondary, Undergraduate, Postgraduate, PhD/Research

### 🔧 Technical Features
- **IBM Cloud API Integration**: Powered by IBM's advanced translation services
- **File Upload Support**: Upload PDF, DOC, DOCX, TXT, PPT, PPTX files
- **RAG-Enhanced Translation**: Retrieves academic glossaries and curriculum frameworks
- **Cultural Context**: Adapts content for regional language nuances
- **Iterative Improvement**: Feedback system for translation refinement
- **Responsive Design**: Modern, mobile-friendly interface

### 📊 Output Features
- **Translated Content**: Main translated text with preserved formatting
- **Glossary of Key Terms**: Subject-specific terminology explanations
- **Cultural Context Notes**: Regional and cultural adaptations
- **Technical Accuracy Notes**: Scientific/mathematical notation preservation

## 🚀 Live Demo

[Deployed on Render](https://your-app-name.onrender.com) *(Replace with your actual deployment URL)*

## 🛠️ Technology Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **API**: IBM Cloud API for translations
- **Deployment**: Render
- **WSGI Server**: Gunicorn
- **File Handling**: Werkzeug

## 📦 Installation

### Prerequisites
- Python 3.10 or higher
- IBM Cloud API key (optional - app works with mocked responses)

### Local Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/multi-lang-translator.git
   cd multi-lang-translator
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set environment variables**
   ```bash
   # Create .env file
   echo "IBM_CLOUD_API_KEY=your_api_key_here" > .env
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Access the application**
   Open your browser and go to `http://localhost:5000`

## 🚀 Deployment on Render

### Step 1: Prepare Repository
Ensure your GitHub repository contains:
- `app.py` (main Flask application)
- `requirements.txt` (dependencies)
- `Procfile` (deployment configuration)
- `runtime.txt` (Python version)
- `render.yaml` (optional deployment config)

### Step 2: Deploy on Render
1. Go to [render.com](https://render.com) and sign up
2. Connect your GitHub repository
3. Create a new **Web Service**
4. Configure settings:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
5. Add environment variable:
   - **Key**: `IBM_CLOUD_API_KEY`
   - **Value**: Your IBM Cloud API key
6. Deploy and wait for build completion

## 📖 Usage Guide

### 1. Access the Application
- Visit the home page to see features and supported languages
- Click "Start Translating" to begin

### 2. Configure Translation
- **Source Language**: Select the original language
- **Target Language**: Choose the desired translation language
- **Subject**: Select the academic subject
- **Content Type**: Choose the type of educational content
- **Academic Level**: Specify the educational level

### 3. Input Content
- **Text Input**: Paste or type course content directly
- **File Upload**: Upload documents (PDF, DOC, DOCX, TXT, PPT, PPTX)
- **Voice Input**: Use voice recognition for text input (browser-supported)

### 4. Get Translation
- Click "Translate Content" to process
- Review the translated content with:
  - Main translated text
  - Glossary of key terms
  - Cultural context notes
  - Technical accuracy notes

### 5. Provide Feedback
- Use the feedback form to suggest improvements
- Submit feedback to refine the translation
- Start new translations as needed

## 🔧 Configuration

### Environment Variables
```bash
IBM_CLOUD_API_KEY=your_ibm_cloud_api_key_here
```

### File Structure
```
multi_lang_translator/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── Procfile             # Render deployment config
├── runtime.txt          # Python version
├── render.yaml          # Render service config
├── utils/
│   └── granite_api.py   # IBM Cloud API integration
├── templates/
│   ├── home.html        # Landing page
│   ├── index.html       # Translation form
│   ├── result.html      # Results page
│   └── feedback.html    # Feedback form
└── static/
    ├── style.css        # Styling
    └── uploads/         # File upload directory
```

## 🔌 API Integration

### IBM Cloud API
The application integrates with IBM Cloud API for advanced translation services:

```python
# Example API call structure
def call_ibm_cloud_api(prompt, api_key):
    url = "https://api.ibm.com/granite/v1/generate"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "prompt": prompt,
        "max_tokens": 1000,
        "temperature": 0.7
    }
    return requests.post(url, headers=headers, json=data)
```

### Fallback System
- If API key is missing: Uses mocked responses
- If API calls fail: Gracefully falls back to mocked responses
- If network issues: Continues with local processing

## 🎨 Features in Detail

### Supported Languages
- **English** ↔ **Hindi**
- **English** ↔ **Marathi**
- **English** ↔ **Tamil**
- **English** ↔ **Bengali**
- **English** ↔ **Telugu**
- **English** ↔ **Kannada**
- **English** ↔ **Gujarati**

### Academic Subjects
- Mathematics, Science, History, Geography
- Literature, Computer Science, Economics
- Political Science, Biology, Chemistry, Physics

### Content Types
- Lecture Notes, Presentation Slides
- Textbook Chapters, Assignments
- Exam Papers, Study Guides, Research Papers

## 🐛 Troubleshooting

### Common Issues

**Build Fails on Render:**
- Ensure all files are committed to GitHub
- Check `requirements.txt` has all dependencies
- Verify `Procfile` is in root directory

**App Doesn't Start:**
- Check Render logs for errors
- Verify `gunicorn app:app` works locally
- Ensure environment variables are set

**API Calls Fail:**
- Verify IBM Cloud API key is correct
- Check API key permissions in IBM Cloud
- App will fall back to mocked responses

**File Upload Issues:**
- Check file size limits
- Verify supported file formats
- Ensure upload directory permissions

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- IBM Cloud for translation API services
- Flask community for the web framework
- Render for hosting services
- Educational institutions for use cases and feedback

## 📞 Support

For support, email support@example.com or create an issue in the repository.

---

**Made with ❤️ for breaking language barriers in education** 