#-*- coding: utf-8 -*-
import requests
from flask import Flask
import Auth
from pprint import pprint
import DefaultSettings
import DbConnectionHandler


# TO DO:
# mistake handling
# going inside dictionary function - simple and transparent!
# print for fetched data?

def search_categories(session, params, search_url, token):
    response = session.get(search_url, params=params)
    data = response.json()

    kategorie_json = []

    kategorie_json = data["categories"]
    kategorie_json["access_token"] = token
    kategorie_json["params"] = params
    print(kategorie_json)
    return kategorie_json


def search_filter(session, params, search_url, token):
    response = session.get(search_url, params=params)
    data = response.json()
    kategorie_json = {}
    kategorie_json['filters'] = data["filters"]
    kategorie_json["access_token"] = token
    kategorie_json["params"] = params
    print(kategorie_json)
    return kategorie_json

def filter_search(session, params, search_url, token):
    # get data with previously established category id and phrase
    response = session.get(search_url, params=params)
    data = response.json()
    print(data['searchMeta'])
    print(data['filters'])
    for filter_dict in data['filters']:
        print(filter_dict)
        print(filter_dict['type'])
        print(filter_dict['name'])

        if filter_dict['type'] == 'MULTI':
            multi_choice(filter_dict, params)

        if filter_dict['type'] == 'TEXT':
            text_choice(filter_dict, params)

        if filter_dict['type'] == 'NUMERIC':
            numeric_choice(filter_dict, params)

        if filter_dict['type'] == 'SINGLE':
            single_choice(filter_dict, params)
        print(params)
    print(params)


def multi_choice(filter_dict, params):

    temp_iter = 1
    temp_dict = []
    for value in filter_dict['values']:
        print(str(list(value.values())[1]) + ' ' + str(list(value.values())[0]) + ' ' + str(temp_iter))

        temp_iter += 1

    # input needs to expect user not to specify some filters, e.g. delivery methods
    choice = input()
    if choice == 'none':
        print('none')
    elif len(choice) > 1:
        choice = choice.split(',')
        print(choice)
        # TODO: fix the loops
        for index in choice:
            print(index)
            temp_dict.append(filter_dict['values'][int(index) - 1])
        print(temp_dict)
        prefix = str(filter_dict['id'])
        multi_list = []
        for value in temp_dict:
            multi_list.append(str(value['value']))

        params[prefix] = multi_list
    elif len(choice) == 1:
        prefix = str(filter_dict['id'])
        params[prefix] = str(filter_dict['values'][int(choice) - 1]['value'])

def single_choice(filter_dict, params):

    temp_iter = 1

    for value in filter_dict['values']:
        print(str(list(value.values())[1]) + ' ' + str(list(value.values())[0]) + ' ' + str(temp_iter))


        temp_iter += 1

    # input needs to expect user not to specify some filters, e.g. delivery methods
    choice = input()
    if choice == 'none':
        print('none')
    else:
        prefix = str(filter_dict['id'])
        temp = filter_dict['values'][int(choice) - 1]
        params[prefix] = temp['value']


def text_choice(filter_dict, params):
    prefix = str(filter_dict['id'])
    choice = input()
    if choice == 'none':
        print('none')
    else:
        params[prefix] = str(choice)


def numeric_choice(filter_dict, params):
    prefix = str(filter_dict['id'])
    for value in filter_dict['values']:
        print(value['name'])
        choice = input()
        if choice != 'none':
            params[prefix + value['idSuffix']] = choice




def finalize_search(params):
    print('podaj mail')
    email = input()
    print('podaj próg cenowy')
    price_treshold = input()
    params['sort'] = '+price'
    params['limit'] = 100
    params['price_threshold'] = price_treshold
    search_string = [params, email]
    return search_string


def search_start(phrase):
    # Main function, will determine set of products, that interest user
    # it will return params dictionary, which contains search phrase, leaf category id and set of filters
    # with params set we can query allegro multiple times every period of time, and get constant results
    # taking into account new items, added after defining search!
    DEFAULT_SEARCH_URL = DefaultSettings.DEFAULT_SEARCH_URL

    headers = Auth.load_default_headers()

    params = {'phrase': phrase}

    with requests.Session() as session:
        session.headers.update(headers)

        return session


        # when displaying filters add count parameter
        # important to distinct filter type e.g. multi or text!
        # filter and category selection will be different in final product, dont bother

    #     filter_search(session, params, DEFAULT_SEARCH_URL)
    #
    #     search_params_list = finalize_search(params)
    #
    # return search_params_list


