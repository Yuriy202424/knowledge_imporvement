from datetime import datetime
from flask import render_template, request, redirect, url_for
from ..db import Coding, Session
from app import app


@app.get('/')
def coding():
    return render_template("coding.html")


@app.post('/')
def coding_data():
    print("POST DATA")
    hours = request.form.get("hours")
    date = datetime.now()
    description = request.form.get("description")
    print("*" * 80)
    print(hours)
    try:
        with Session.begin() as session:
            code = Coding(hours=hours, date=date, description=description)
            session.add(code)
            session.commit()
        
        return redirect(url_for("result"))
    
    except Exception as e:
        print(f"Error: {e}")