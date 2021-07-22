import requests, math

def avgRotorSpeed(statusQuery, parentId):
    # Write your code here
    statusQuery = statusQuery
    url = "https://jsonmock.hackerrank.com/api/iot_devices/search?status=" + statusQuery #+ "&page=" + number
    url_ = url + "&page=" + str(1) 
    response = requests.get(url_)
    # print(response)
    # print(response.json())
    datas = response.json()['data']
    
    for i in range(2, response.json()['total_pages'] + 1):
        url_ = url + "&page=" + str(i)
        response = requests.get(url)
        print(response)
        datas += response.json()['data']
    print("-----------------")
    # print(datas)
    # print("done")
    count = 0
    total = 0
    for data in datas:
        # print(data)
        if data.get('parent') != None:
            parent = data['parent']
            # print("doajodaod")
            # print(parent)
            if parent['id'] == 2:
                print(data)
                count += 1
                total += data["operatingParams"]["rotorSpeed"]
    if count == 0:
        return 0
    return math.floor(total / count)
avgRotorSpeed("RUNNING", 7)