from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    # Real news list with links
    jobs = [
        {"title": "HCL Graduate Trainee", "loc": "Chennai", "link": "#"},
        {"title": "ZOHO Software Engineer", "loc": "Tenkasi", "link": "#"},
        {"title": "TCS Smart Hiring 2026", "loc": "Remote", "link": "#"}
    ]
    
    # Professional UI Design
    html = """
    <html>
    <body style="font-family: 'Segoe UI', sans-serif; background-color: #eef2f7; text-align: center; padding: 50px;">
        <h1 style="color: #2c3e50;">🚀 Students Job Portal 2026</h1>
        <p style="color: #7f8c8d;">Latest career opportunities for you</p>
        
        <div style="display: flex; justify-content: center; gap: 20px; flex-wrap: wrap; margin-top: 30px;">
    """
    
    for j in jobs:
        html += f"""
        <div style="background: white; padding: 20px; border-radius: 12px; width: 250px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); border-top: 5px solid #3498db;">
            <h3 style="margin: 0; color: #34495e;">{j['title']}</h3>
            <p style="color: #95a5a6;">📍 {j['loc']}</p>
            <a href="{j['link']}" style="background: #3498db; color: white; text-decoration: none; padding: 10px 20px; border-radius: 5px; display: inline-block;">Apply Now</a>
        </div>
        """
        
    html += "</div></body></html>"
    return html

if __name__ == '__main__':

    app.run(host='0.0.0.0',port=10000)
