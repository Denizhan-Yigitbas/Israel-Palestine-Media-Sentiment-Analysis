# from newsapi import NewsApiClient

# Init
# newsapi = NewsApiClient(api_key='beeda840e903432e8123519ec509f3bf')


# # /v2/everything
# all_articles = newsapi.get_everything(q='israel', from_param='2017-12-01', to='2017-12-12',)

# print(len(all_articles))

# curl -XGET 'api.datanews.io/v1/headlines?q=Israel%20US%2

# import pprint
# import requests 

# secret = 'beeda840e903432e8123519ec509f3bf'
# url = 'https://newsapi.org/v2/everything?'

# parameters = {
#     'q': 'US Embassy in Jerusalem', # query phrase
#     'pageSize': 20,  # maximum is 100
#     'apiKey': secret, # your own API key
#     'from': '2008-11-22',
#     'to' : '2020-11-22',
#     'source': "TechCrunch"
# }

# # Make the request
# response = requests.get(url, params=parameters)

# # Convert the response to JSON format and pretty print it
# response_json = response.json()
# pprint.pprint(response_json)

# for i in response_json['articles']:
#     print(i['title'])
