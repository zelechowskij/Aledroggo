from flask import Flask, render_template, request
import define_search
import DefaultSettings
import Auth
import requests
import json
import DbConnectionHandler
import os
from flask import jsonify, make_response
import phase2

os.environ['LD_LIBRARY_PATH'] = '/srv/instantclient'

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template("main.html")


@app.route('/token', methods=['POST', "GET"])
def token():
    token = Auth.get_client_credentials_flow_access_token()
    return render_template("search_start.html", token=token)


@app.route('/search_start', methods=['POST', "GET"])
def searchstart():
    token = Auth.get_client_credentials_flow_access_token()
    return render_template("search_start.html", token=token)

@app.route('/search_history', methods=['POST', "GET"])
def searchhistory():

    return "To be announced"

@app.route('/phrase', methods=['POST'])
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

        json = define_search.search_categories(session, params, DEFAULT_SEARCH_URL, access_token)

    # TODO: else 0 subcat
    print(json)
    if len(json['subcategories']) == 1:
        return filters(json)

    else:
        return render_template("category.html", json=json)


@app.route('/filter', methods=['POST'])
def filters(json_element):
    DEFAULT_SEARCH_URL = DefaultSettings.DEFAULT_SEARCH_URL

    params = json_element['params']
    access_token = json_element["access_token"]
    headers = headers = {"charset": "utf-8", "Accept-Language": "pl-PL", "Content-Type": "application/json",
                         "Accept": 'application/vnd.allegro.public.v1+json',
                         "Authorization": "Bearer {}".format(json_element['access_token'])}
    with requests.Session() as session:
        session.headers.update(headers)
        json_element = define_search.search_filter(session, params, DEFAULT_SEARCH_URL, access_token)

    return render_template("filter.html", json=json_element)


# TODO: template inheritance e.g. navbar etc


@app.route('/email', methods=['POST'])
def email():
    params = request.form['params']
    params = params.replace("'", "\"")
    params = json.loads(params)

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

    parameters = {'params': params}

    return render_template("email.html", params=parameters)


@app.route('/final', methods=['POST'])
def final():
    data = request.form.copy()
    parameters = data['parameters']
    parameters = parameters.replace("'", "\"")
    for item in data:
        print(item)
        print(data[item])
    email = data['email']
    params = json.loads(parameters)
    params['sort'] = '+price'
    params['limit'] = 100
    params['price_threshold'] = data['price_threshold']
    print(params)
    search_string = [params, email]
    DbConnectionHandler.update_search_table(search_string)
    return render_template("final.html")

@app.route('/dQw4w9WgXcQ', methods=['GET'])
def job():
    phase2.check_allegro()
    data = {'message': 'Checked', 'code': 'SUCCESS'}
    return make_response(jsonify(data), 201)



if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=5000, debug=True)
