from flask import Flask, render_template, request
from spotify_api import get_access_token, refresh_token
from screen import update_screen
import os
import ast
import webbrowser
import threading
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")


def get_token_data():
    get_data = True
    while get_data:        
        token_request = get_access_token()
        if token_request[0]["access_token"]:
            get_data = False        
    return token_request

token_request = get_token_data()

token_request[0]['refresh'] = False

with open('refresh-data.txt', 'w') as refresh_data:
    refresh_data.write(str(token_request))
    refresh_data.close()


def open_browser():
    webbrowser.open_new('http://127.0.0.1:5000')


@app.route("/")
def home():

    return render_template("index.html")

@app.route("/screen", methods=["POST"])
def update():    
    
    new_dict = request.form.to_dict()
                
    with open("data.txt", "r") as playback_data:
        data_dict = ast.literal_eval(playback_data.read())
        img_url = data_dict['img']
        playback_data.close()           

    if new_dict["img"] != img_url:
        update_screen(new_dict)            
        with open("data.txt", "w") as playback_data:            
            playback_data.write(str(new_dict))
            playback_data.close()
            
    return ('', 200)

@app.route("/callback")
def callback():
      
    with open('refresh-data.txt', 'r') as refresh_data:
        token_data = ast.literal_eval(refresh_data.read())
        refresh_data.close()
       
    if token_data[0]["refresh"]:
        new_token = refresh_token(refresh_token=token_data[0]['refresh_token'], 
                                  headers=token_data[1])        
        return new_token
    else:
        token_data[0]["refresh"] = True
        with open('refresh-data.txt', 'w') as refresh_data:
            refresh_data.write(str(token_data))
            refresh_data.close()       
        return token_data[0]['access_token']
    

if __name__ == '__main__':
    threading.Timer(1, open_browser).start()
    app.run(debug=False)
