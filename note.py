from flask import Flask, render_template, request, session

from flask_session import Session

app=Flask(__name__)

app.config["SESSION_PERMANENT"]=False

app.config["SESSION_TYPE"]="filesystem"

Session(app)

@app.route("/", methods=["GET","POST"])

def index():
    if session.get("notes") is None:
        session["notes"]=[]
    if request.method=="POST":
        note=request.form.get("note")
        note=note.strip()
        len(note) !=0
        if True:
            if note in session["notes"]:
                pass
            else:
                session["notes"].append(note)

    return render_template("daily_notes.html", notes=session["notes"])
