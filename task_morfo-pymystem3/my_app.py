from flask import Flask, render_template, request
from analize import get_glagols


app = Flask(__name__)

result_dict = {}

@app.route('/')
def index():
    if request.args:
        text = request.args['text']
        result = get_glagols(text)
        return render_template('index.html', result=result, text=text)
    #рисуем форму
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)