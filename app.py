from flask import Flask, request, render_template, jsonify, send_from_directory, redirect
import os

from modules.draw import draw




app = Flask(__name__)
PEOPLE_FOLDER = os.path.join('result', '')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result/<path:filename>')
def image(filename):
    return send_from_directory("result", filename, as_attachment=('download' in request.args))



@app.route('/show/<path:filename>')
def show(filename):
    file = os.path.join('result', filename + ".png")
    if os.path.exists(file):
        return render_template("show.html", image=filename)
    else:
        return render_template('404.html'), 404

@app.route('/make_by_text/<text>')
def make_by_text(text):
    semple_input = '1'
    name = draw(semple_input, text)
    return redirect('/show/' + name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(debug=True)



