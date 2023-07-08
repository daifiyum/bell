import base64, json
import requests
from blog import models
from django.conf import settings

user = settings.ZINCSEARCH['user']
password = settings.ZINCSEARCH['password']
bas64encoded_creds = base64.b64encode(bytes(user + ":" + password, "utf-8")).decode("utf-8")
headers = {"Content-type": "application/json", "Authorization": "Basic " + bas64encoded_creds}
index = settings.ZINCSEARCH['index']
zinc_host = settings.ZINCSEARCH['zinc_host']

# 添加索引
def addIndex(id):
    zinc_url = zinc_host + "/api/" + index + "/_doc/" + str(id)
    newPost = models.Post.objects.filter(id = id).first()
    data = { 
        "title": newPost.title,
        "content": newPost.content 
    }
    res = requests.put(zinc_url, headers=headers, data=json.dumps(data))

# 更新索引
def updateIndex(id):
    zinc_url = zinc_host + "/api/" + index + "/_update/" + str(id)
    newPost = models.Post.objects.filter(id = id).first()
    data = { 
        "title": newPost.title,
        "content": newPost.content 
    }
    res = requests.post(zinc_url, headers=headers, data=json.dumps(data))

# 删除索引
def delIndex(id):
    zinc_url = zinc_host + "/api/blog/" + "_doc/" + str(id)
    res = requests.delete(zinc_url, headers=headers)

# 搜索
def searchIndex(keys):
    zinc_url = zinc_host + "/api/blog/_search"
    data = {
        "search_type": "matchphrase",
        "query":
        {
            "term": keys
        },
        "from": 0,
        "max_results": 100,
        "_source": []
    }
    res = requests.post(zinc_url, headers=headers, json=data)
    result = []
    for i in res.json()['hits']['hits']:
        result.append(int(i['_id']))
    return result



# 初始化索引数据库

# 创建索引库
def createIndex():
    zinc_url = zinc_host + "/api/index"
    data = {
        "name": index,
        "storage_type": "disk",
        "shard_num": 1,
        "mappings": {
            "properties": {
                "title": {
                    "type": "text",
                    "index": True,
                    "store": True,
                    "highlightable": False
                },
                "content": {
                    "type": "text",
                    "index": True,
                    "store": True,
                    "highlightable": False
                },
            }
        }
    }
    res = requests.post(zinc_url, headers=headers, data=json.dumps(data))

# 初始化索引库
def initIndex():
    zinc_url = zinc_host + "/api/index_name?name=" + index
    try:
        res = requests.get(zinc_url, headers=headers)
        if res.status_code == 200:
            if not res.json():
               createIndex()
        return True

    except:
        print("无法连接 zincsearch 搜索引擎，索引数据库初始化失败！")
        return False