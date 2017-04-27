from flask import Flask, render_template, request
from analize import get_glagols
from vkapi import Group

app = Flask(__name__)

result_dict = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/glagols')
def glagols():
    if request.args:
        text = request.args['text']
        result = get_glagols(text)
        return render_template('glagols.html', result=result, text=text, page='glagols')
    #рисуем форму
    return render_template('glagols.html', page='glagols')

@app.route('/api')
def api():
    if request.args:
        id1 = request.args['g1_id']
        g1 = Group(id1)
        id2 = request.args['g2_id']
        g2 = Group(id2)
        if not g1.errors and not g2.errors:
            #общие подписчики
            both_users = len([u for u in g1.users if u in g2.users])
        else:
            both_users = None
        return render_template('api.html', g1=g1, g2=g2, both_users=both_users, result=True)
    return render_template('api.html', page='api')


if __name__ == '__main__':
    app.run(debug=True)