from datetime import datetime
from flask import render_template, request, redirect, url_for
from ..db import Coding, Session
from app import app



@app.get("/")
def index():
    return render_template("coding.html")


@app.post("/")
def post_data():
    try:
        hours = int(request.form.get('hours'))
        date = datetime.now()
        description = request.form.get("description")
        
        with Session.begin() as session:
            data = Coding(hours=hours, date=date, description=description)
            session.add(data)
        return redirect(url_for("result"))
    except Exception as e:
        print(f"Error: {e}")
        return "There was an error."
