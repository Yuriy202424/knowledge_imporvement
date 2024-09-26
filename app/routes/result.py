from flask import render_template, request
from sqlalchemy import select
from app import app
from ..db import Coding, Session


@app.get("/result")
def result():
    print(" RESULT ")
    try:
        with Session.begin() as session:
            result = session.execute(select(Coding.date, Coding.hours, Coding.description)).all()
        
        results = [{'date': row[0], 'hours': row[1], 'description': row[2]} for row in result]
        print(results)
        return render_template('result.html', values=results)
    
    except Exception as e:
        print(f"Error: {e}")
        return "An error occurred", 500

