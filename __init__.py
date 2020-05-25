from flask import Flask, render_template, request, jsonify
import define_search
import DefaultSettings
import Auth
import requests
import json

app = Flask(__name__)
isFirst = True
@app.route('/')
def homepage():
    return render_template("main.html")


@app.route('/search_start', methods = ['POST', "GET"])
def searchstart():

    token = Auth.get_access_token()
    return render_template("search_start.html", token = token)


@app.route('/phrase', methods = ['POST'])
def phrase():
    phrase = request.form['phrase']
    if "token" in request.form:
        access_token = request.form["token"]

    print(request.form)
    if "category.id" in request.form:

        category = request.form['category.id']
        params = {'phrase': phrase, 'category.id': category}

    else:
        params = {'phrase': phrase}

    DEFAULT_SEARCH_URL = DefaultSettings.DEFAULT_SEARCH_URL
    headers = headers = {"charset": "utf-8", "Accept-Language": "pl-PL", "Content-Type": "application/json",
               "Accept": 'application/vnd.allegro.public.v1+json',
               "Authorization": "Bearer {}".format(access_token)}
    with requests.Session() as session:
        session.headers.update(headers)

        json =  define_search.search_categories(session, params, DEFAULT_SEARCH_URL, access_token)

    # TODO: else 0 subcat

    if len(json['subcategories']) == 1:
        return filters(json)

    else:
        return render_template("category.html", json = json)


@app.route('/filter', methods = ['POST'])
def filters(json):
    DEFAULT_SEARCH_URL = DefaultSettings.DEFAULT_SEARCH_URL

    params = json['params']
    access_token = json["access_token"]
    headers =headers = {"charset": "utf-8", "Accept-Language": "pl-PL", "Content-Type": "application/json",
               "Accept": 'application/vnd.allegro.public.v1+json',
               "Authorization": "Bearer {}".format(json['access_token'])}
    with requests.Session() as session:
        session.headers.update(headers)
        json = define_search.search_filter(session, params, DEFAULT_SEARCH_URL, access_token)

    return render_template("filter.html", json = json)

# TODO: template inheritance e.g. navbar etc


@app.route('/email', methods = ['POST'])
def email():
    params = request.form['params']
    params = params.replace("'", "\"")
    params = json.loads(params)

    token = request.form['token']
    data = request.form.copy()
    data.pop('params')
    data.pop('token')
    for item in data:
        # czy jest jakaś wartość dla klucza
        if len(data[item]) != 0:
            # czy nie ma wiecej niz jednej wartości dla danego klucza
            if data[item] == "brak":
                continue

            if len(data.getlist(item)) > 1:
                temp_list = data.getlist(item)
                params[item] = temp_list

            else:
                params[item] = data[item]

    parametry = {}
    parametry['params'] = params
    print(parametry)
    return render_template("email.html", params = parametry)

@app.route('/final', methods = ['POST'])
def final():
    data = request.form.copy()
    for item in data:
        print(item)
        print(data[item])
    return render_template("final.html")


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=5000, debug=True)