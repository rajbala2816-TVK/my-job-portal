from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
   
    sections = [
        "முகப்புப் பக்கம் (Home)", "டவுட் கிளியரிங் (Doubt Clearing)", 
        "டிஸ்கஷன் ஃபோரம் (Discussion)", "புராஜெக்ட் ஐடியாஸ் (Projects)", 
        "வேலைவாய்ப்பு (Jobs)", "காலேஜ் நியூஸ் (College News)", 
        "ஆர்டிகிள்ஸ் (Articles)", "தொடர்பு (Contact)"
    ]
    
    html = """
    <html>
    <head>
        <title>Muthuraj College Portal</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body { font-family: Arial; background: #f4f4f4; text-align: center; padding: 20px; }
            .grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 15px; margin-top: 20px; }
            .box { background: #007bff; color: white; padding: 30px 10px; border-radius: 10px; text-decoration: none; font-weight: bold; font-size: 14px; }
            h1 { color: #333; }
        </style>
    </head>
    <body>
        <h1>Muthuraj College Portal</h1>
        <div class="grid">
    """
    
    for item in sections:
        html += f'<a href="#" class="box">{item}</a>'
        
    html += """
        </div>
    </body>
    </html>
    """
    return html

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
