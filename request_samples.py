import requests

if __name__ == "__main__":
    payload = {'client_id': '2751304604', 'client_secret': "3732bbd1292705621b5344f7f912d4bc", 'grant_type': "authorization_code", 'redirect_uri': "http://127.0.0.1:8000/weibo_auth_callback", 'code': "efa615010e253e23068441cc9e5695ee"}
    # url = "https://api.weibo.com/oauth2/access_token?client_id=%s&client_secret=%s&grant_type=authorization_code&redirect_uri=%s&code=%s" % ("2751304604","3732bbd1292705621b5344f7f912d4bc","http://127.0.0.1:8000/weibo_auth_callback","efa615010e253e23068441cc9e5695ee")
    # print url
    r = requests.post("https://api.weibo.com/oauth2/access_token",payload)
    print dir(r)
    print r.text
    print "Http code: %d\nText:%s" % (r.status_code, r.text)