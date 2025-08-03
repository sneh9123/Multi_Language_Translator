import os
from flask import Flask, render_template, request, url_for
from werkzeug.utils import secure_filename
from utils.granite_api import translate_course_content

# App configuration
UPLOAD_FOLDER = 'static/uploads'
app = Flask(__name__, static_url_path='/static')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/form')
def form():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    user_data = {
        "source_language": request.form['source_language'],
        "target_language": request.form['target_language'],
        "subject": request.form['subject'],
        "content_type": request.form['content_type'],
        "academic_level": request.form['academic_level']
    }

    # Handle uploaded document
    document = request.files.get('course_document')
    document_filename = None
    if document and document.filename != '':
        document_filename = secure_filename(document.filename)
        document.save(os.path.join(app.config['UPLOAD_FOLDER'], document_filename))

    # Handle text content
    text_content = request.form.get('text_content', '').strip()

    # Handle feedback from previous response (if present)
    feedback_text = request.form.get("feedback", "").strip()

    # Get translated content using Granite with optional feedback
    translated_content = translate_course_content(
        user_data, 
        text_content=text_content,
        document_filename=document_filename,
        feedback=feedback_text
    )

    return render_template(
        'result.html',
        translated_content=translated_content,
        document_filename=document_filename,
        user_data=user_data
    )

# Optional route to handle feedback POST separately (if using JS/AJAX)
@app.route('/feedback', methods=['POST'])
def feedback():
    return render_template('index.html')  # Or redirect with pre-filled values

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 