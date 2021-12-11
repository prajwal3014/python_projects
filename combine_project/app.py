from flask import Flask, request, render_template, redirect, url_for
from Calculator_GUI_project.gui_calculator import calculator
from Youtube_video_downloader.youtube_downloader import window_main

app = Flask(__name__)
app.secret_key = 'COMBINING ALL PROJECTS'

@app.route('/')
def index() :
    return render_template('index.html')

@app.route('/Calculator')
def to_calculator() :
    calculator()
    return redirect(url_for('index'))

@app.route('/Youtube')
def to_youtube() :
    window_main()
    return redirect(url_for('index'))

if __name__ == "__main__" :
    app.run(debug=True)