from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    sections = [
        ("Home Page", "/"), ("Doubt Clearing", "/work"), 
        ("Discussion Forum", "/work"), ("Project Ideas", "/work"), 
        ("Jobs & Internships", "/jobs"), ("College News", "/work"), 
        ("Articles", "/work"), ("Contact Us", "/work")
    ]
    
    html = """
    <html>
    <head>
        <title>College Portal</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body { font-family: sans-serif; background: #f0f2f5; text-align: center; padding: 20px; }
            .grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 12px; }
            .box { background: #1e3c72; color: white; padding: 40px 10px; border-radius: 15px; text-decoration: none; font-weight: bold; }
        </style>
    </head>
    <body>
        <h1>College Portal</h1>
        <div class="grid">
    """
    for name, link in sections:
        html += f'<a href="{link}" class="box">{name}</a>'
    html += "</div></body></html>"
    return html


@app.route('/jobs')
def jobs():
    return "<h2>Jobs Page Coming Soon!</h2><a href='/'>Back to Home</a>"


@app.route('/work')
def work():
    return "<h2>This section is under development!</h2><a href='/'>Back to Home</a>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
