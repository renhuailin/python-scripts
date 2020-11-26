# -*- coding: utf-8 -*-

import requests
import pprint
import os

# 10 => Guest access
# 20 => Reporter access
# 30 => Developer access
# 40 => Maintainer access
# 50 => Owner access
AccessLevels = {10: "Guest", 20: "Reporter",
                30: 'Developer', 40: 'Maintainer', 50: 'Owner'}


userDict = {}

gitlabToken= os.environ.get('GITLAB_TOKEN', "")

def getUsers(page: int):
    headers = {'PRIVATE-TOKEN': gitlabToken}
    payload = {'per_page': 100, "page": page}
    url = "http://140.143.213.65/api/v4/users"
    r = requests.get(url, headers=headers, params=payload)
    print(len(r.json()))

    return r.json()


def getProjectsOfUser(userId: int):

    headers = {'PRIVATE-TOKEN': gitlabToken}

    url = "http://140.143.213.65/api/v4/users/%s/projects" % userId
    r = requests.get(url, headers=headers)
    print(r.json())
    print(len(r.json()))

    return r.json()


def getProjectsOfGroup(groupId: int, page: int):

    headers = {'PRIVATE-TOKEN': gitlabToken}
    payload = {'per_page': 100, "page": page}
    url = "http://140.143.213.65/api/v4/groups/%s/projects" % groupId
    r = requests.get(url, headers=headers, params=payload)
    print(r.json())
    print(len(r.json()))

    return r.json()


def getProjects(page: int):
    headers = {'PRIVATE-TOKEN': gitlabToken}
    payload = {'per_page': 100, "page": page}
    url = "http://140.143.213.65/api/v4/projects"
    r = requests.get(url, headers=headers, params=payload)
    # print(r.json())
    print(len(r.json()))

    return r.json()


def getMembersOfProject(projectId: int):
    headers = {'PRIVATE-TOKEN': gitlabToken}
    # payload = {'per_page': 100, "page": page, "simple": 'true'}
    url = "http://140.143.213.65/api/v4/projects/%s/members" % projectId
    r = requests.get(url, headers=headers)
    # print(r.json())
    # print(len(r.json()))

    return r.json()


def getMembersOfGroup(groupId: int, page: int):
    headers = {'PRIVATE-TOKEN': gitlabToken}
    payload = {'per_page': 100, "page": page}
    url = "http://140.143.213.65/api/v4/groups/%s/members" % groupId
    r = requests.get(url, headers=headers, params=payload)
    # print(r.json())
    # print(len(r.json()))

    return r.json()


def getGroups(page: int):
    headers = {'PRIVATE-TOKEN': gitlabToken}
    payload = {'per_page': 100, "page": page}
    url = "http://140.143.213.65/api/v4/groups"
    r = requests.get(url, headers=headers, params=payload)
    # print(r.json())
    print(len(r.json()))

    return r.json()


# users = getUsers(1)
# for user in users:
#     print("id=%d name=%s" % (user['id'], user['name']))


# projects = getProjectsOfUser(439)

# Get projects of a group 236
# projects = getProjectsOfGroup(236)

# # projects = getProjects(1)

# for project in projects:

#     print(project)
#     print("Project id=%d name=%s" % (project['id'], project['name']))
#     members = getMembersOfProject(project['id'])
#     for user in members:
#         print("id=%d name=%s Role= %s" %
#               (user['id'], user['name'], AccessLevels[user['access_level']]))


# Get all users
for i in range(100):
    users = getUsers(page=i)
    if len(users) < 1:
        break

    for user in users:
        user['projects'] = {}
        userDict[user['id']] = {"id": user['id'], "name": user['name'],
                                "email": user['email'], 'username': user['username'], 'state': user['state'], 'projects': {}}


# print(userDict)

for i in range(100):
    projects = getProjects(page=i)
    if len(projects) < 0:
        break

    for project in projects:

        print(project)
        print("Project id=%d name=%s" % (project['id'], project['name']))
        members = getMembersOfProject(project['id'])
        for user in members:
            print("id=%d name=%s Role= %s" %
                  (user['id'], user['name'], AccessLevels[user['access_level']]))

            userDict[user['id']]['projects'][project['id']] = {
                "project": {'id': project['id'], 'name': project['name'], 'web_url': project['web_url']}, "access_level": AccessLevels[user['access_level']]}


# Get all groups
for i in range(100):
    groups = getGroups(page=i)
    if len(groups) < 1:
        break

    for group in groups:
        # Get projects of this group
        groupProjects = []
        for j in range(1000):
            projects = getProjectsOfGroup(groupId=group['id'], page=j)
            if len(projects) < 1:
                break
            groupProjects += projects

        # Get members of this group
        for j in range(1000):
            members = getMembersOfGroup(groupId=group['id'], page=j)
            if len(members) < 1:
                break

            for user in members:
                # print("id=%d name=%s Role= %s" %
                #       (user['id'], user['name'], AccessLevels[user['access_level']]))
                print("id=%d name=%s Role= %s" %
                      (user['id'], user['name'], user['access_level']))
                for project in groupProjects:
                    userDict[user['id']]['projects'][project['id']] = {
                        "project":  {'id': project['id'], 'name': project['name'], 'web_url': project['web_url']}, "access_level": AccessLevels[user['access_level']]}

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(userDict)

if __name__ == '__main__':
    pass
