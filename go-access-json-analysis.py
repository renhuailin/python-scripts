# -*- coding: utf-8 -*-
#  这个脚本是统计Go Access Json中的数据，用以分析CDP的相关服务的请求数。


import json


services = {}


with open('/Users/harley/Downloads/goaccess-1598420292999.json') as json_file:
    data = json.load(json_file)
    for p in data['requests']['data']:
        
        url = p['data'].split('/')
        if len(url) < 2 :
            continue

        servicePath = url[1]

        if not servicePath in services:
            services[servicePath] = p['hits']['count']
        else:
            services[servicePath] += p['hits']['count']
        # print('data: ' + p['data'])
        # print('')


for k, v in services.items():
    if v > 100:
        print("Service: %s      Count: %d" % (k, v))
# batches = json.loads()
