from flask import Flask, render_template, request, jsonify
import define_search
app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template("main.html")


@app.route('/search_start', methods = ['POST', "GET"])
def searchstart():
    # if request.method == "POST":
    #     phrase = request.form["phrase"]
    #     return render_template("search_start.html")
    # else:
    #     return render_template("search_start.html")
    return render_template("search_start.html")


@app.route('/phrase', methods = ['POST'])
def phrase():
    phrase = request.form['phrase']
    define_search.search_start(phrase)
    return jsonify({'result': 'success'})


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=5000, debug=True)