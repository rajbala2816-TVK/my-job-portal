from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    
    sections = [
        ("Home Page", "/"), 
        ("Doubt Clearing", "/work"), 
        ("Discussion Forum", "/work"), 
        ("Project Ideas", "/work"), 
        ("Jobs & Internships", "/jobs"), 
        ("College News", "/work"), 
        ("Articles", "/work"), 
        ("Contact Us", "/work")
    ]
    
    html = """
    <html>
    <head>
        <title>College Portal</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body { font-family: sans-serif; background: #f0f2f5; text-align: center; padding: 20px; }
            .grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 12px; max-width: 500px; margin: 0 auto; }
            .box { 
                background: #1e3c72; 
                color: white; 
                padding: 40px 10px; 
                border-radius: 15px; 
                text-decoration: none; 
                font-weight: bold; 
                font-size: 14px;
                box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            }
            .box:active { background: #2a5298; transform: scale(0.95); }
            h1 { color: #1e3c72; }
        </style>
    </head>
    <body>
        <h1>College Portal</h1>
        <p>Student Dashboard</p>
        <div class="grid">
    """
    for name, link in sections:
        html += f'<a href="{link}" class="box">{name}</a>'
    html += "</div></body></html>"
    return html


@app.route('/jobs')
def jobs():
    return """
    <div style="text-align:center; padding:50px;">
        <h2>Jobs & Internships Page</h2>
        <p>TCS, HCL, ZOHO jobs list will be here soon!</p>
        <a href="/" style="padding:10px; background:#1e3c72; color:white; text-decoration:none; border-radius:5px;">Back to Home</a>
    </div>
    """


@app.route('/work')
def work():
    return """
    <div style="text-align:center; padding:50px;">
        <h2>Working on it...</h2>
        <p>This section is coming soon!</p>
        <a href="/" style="padding:10px; background:#1e3c72; color:white; text-decoration:none; border-radius:5px;">Back to Home</a>
    </div>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
