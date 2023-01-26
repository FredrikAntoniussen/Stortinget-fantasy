from flask import Flask, render_template, request
import json

app = Flask(__name__)



fil = open("politikere.json", encoding="utf-8") # må ha encoding="utf-8" for å tolke tegn som æ,ø,å i filen
userFil = open("politikere.json", encoding="UTF-8")
politikerliste= json.load(fil)
users = json.load(userFil)



@app.route("/")
def index():
    
    return render_template("index.html",politikerliste = politikerliste)