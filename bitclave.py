import requests

hashid = '0x37261284f818e90516737e7fcb74980b926e11f6c51cf59c845cda3af80e0179'
query_url = 'https://desearch.com/api/search/v2?request='
key_list = ('data', 'type','source','currency')
response = requests.get(query_url+hashid)

# Here we get response status 10x,20x,30x,40x,50x
def query_status(x):
    return x.status_code

# Here we check is basic dictionary keys appears in response
def check_dict(s):
    for f in key_list:
        if f not in s:
            print (f, ' is not in dictionary')

# If our request return not good status (200) or return empty json need to return error
if query_status(response) != 200 or not response.json():
     print ('Something goes wrong','\n',response,'\n','Content is ',response.content)
     exit()

json_dict = response.json()[0]
check_dict(json_dict.keys())