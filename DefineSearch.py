import requests
import Auth
from pprint import pprint
import csv


# TO DO:
# mistake handling
# going inside dictionary function - simple and transparent !
# print for fetched data

def searchStart():
    DEFAULT_SEARCH_URL = Auth.DEFAULT_API_URL + "/offers/listing"

    headers = {"charset": "utf-8", "Accept-Language": "pl-PL", "Content-Type": "application/json",
               "Accept": 'application/vnd.allegro.public.v1+json',
               "Authorization": "Bearer {}".format(Auth.access_token)}
    phrase = "xiaomi redmi note 8 pro"
    category = "300525"
    filter_temp = ''
    params = {"phrase": phrase, 'category.id': category}

    with requests.Session() as session:
        session.headers.update(headers)
        data = {'categories': {'subcategories': [{'id': 'temp'}, {'id': 'temp2'}]}}

        while len(data['categories']['subcategories']) != 1:
            response = session.get(DEFAULT_SEARCH_URL, params=params)
            data = response.json()

            for categorie in data["categories"]["subcategories"]:
                pprint(categorie["name"] + ' ' + categorie["id"])

            temp_category = input()
            params["category.id"] = temp_category

        # when displaying filters add count parameter
        # important to distinct filter type e.g. multi or text!
        # filter and category selection will be different in final product, dont bother
        filter_temp = ''
        temp_dict = []
        for filter in data['filters']:
            print(filter)
            print(filter['name'])
            if filter['type'] == 'MULTI':

                # POGMATWANE TO MAX WEŹ TO NAPRAW!
                temp_iter = 1
                for value in filter['values']:
                    print(str(list(value.values())[1]) + ' ' + str(list(value.values())[0]) + ' ' + str(temp_iter))
                    # temp_dict.append(dict(value = str(list(value.values())[1]), name = str(list(value.values())[0])))
                    # POGMATWANE TO MAX WEŹ TO NAPRAW!
                    temp_iter += 1

                # input needs to expect user to not specify some filters, e.g. delivery methods
                choice = input()
                if choice == 'none':
                    print('none')
                    continue
                else:
                    choice = choice.split(',')
                    for index in choice:
                        temp_dict.append(filter['values'][int(index) - 1])
                    print(temp_dict)
            filter_temp = '?'
            # boolean flag!
            first = True
            for value in temp_dict:
                if first:
                    filter_temp = filter_temp + filter['id'] + '=' + value['value']

                else:
                    filter_temp = filter_temp + '&' + filter['id'] + '=' + value['value']
                first = False
            print(filter_temp)
        print(filter_temp)
        # with open(filter.csv, 'w') as f:
        #     for key in filter_temp.keys():
        #         f.write("%s,%s\n" % (key, filter_temp[key]))

            # POGMATWANE TO MAX WEŹ TO NAPRAW!
            # choice = input()
            # choice = choice.split(',')

            # for value in filter['values']:
            #     print(str(list(value.values())[1]) + ' ' + str(list(value.values())[0]))
            #
            # choice = input()


searchStart()
