from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    sections = [
        "Home Page", "Doubt Clearing", 
        "Discussion Forum", "Project Ideas", 
        "Jobs & Internships", "College News", 
        "Articles", "Contact Us"
    ]
    
    html = """
    <html>
    <head>
        <title>Muthuraj College Portal</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body { font-family: 'Segoe UI', sans-serif; background: #f0f2f5; text-align: center; padding: 20px; margin: 0; }
            h1 { color: #1a73e8; margin-top: 20px; font-size: 24px; }
            p { color: #5f6368; margin-bottom: 25px; }
            .grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 12px; max-width: 500px; margin: 0 auto; }
            /* இங்க தான் கலர் மாத்தியிருக்கேன் - Royal Blue & Gradient */
            .box { 
                background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%); 
                color: white; 
                padding: 40px 10px; 
                border-radius: 15px; 
                text-decoration: none; 
                font-weight: 600; 
                font-size: 14px; 
                box-shadow: 0 4px 15px rgba(0,0,0,0.1);
                display: flex;
                align-items: center;
                justify-content: center;
                transition: transform 0.2s;
            }
            .box:active { transform: scale(0.95); opacity: 0.9; }
        </style>
    </head>
    <body>
        <h1>College Student Portal</h1>
        <p>Your Academic Dashboard</p>
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

