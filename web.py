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
            body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #eef2f3; text-align: center; padding: 20px; }
            .grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 15px; margin-top: 25px; }
            .box { background: #2c3e50; color: white; padding: 35px 10px; border-radius: 12px; text-decoration: none; font-weight: bold; font-size: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
            .box:active { background: #1a252f; transform: scale(0.98); }
            h1 { color: #2c3e50; margin-bottom: 5px; }
            p { color: #7f8c8d; margin-top: 0; }
        </style>
    </head>
    <body>
        <h1>College Portal</h1>
        <p>Welcome to Student Dashboard</p>
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

