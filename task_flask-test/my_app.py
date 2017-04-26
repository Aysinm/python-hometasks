from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

result_dict = {}

@app.route('/')
def index():
    if request.args:
        name = request.args['name']
        optradio = request.args['optradio']
        if name in result_dict:
            result_dict[name].append(optradio)
        else:
            result_dict[name] = [optradio]
        return redirect(url_for('result'))
    return render_template('index.html')


@app.route('/result')
def result():
    cats_count = 0
    dogs_count = 0
    count_dict = {}
    for k, v in result_dict.items():
        count_dict[k] = len(v)
        for r in v:
            if r == 'cat':
                cats_count+=1
            elif r == 'dog':
                dogs_count+=1
    return render_template('result.html', count_dict=count_dict, dogs_count=dogs_count, cats_count=cats_count)

if __name__ == '__main__':
    app.run(debug=True)