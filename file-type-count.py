#! /usr/bin/python3
# -*- coding: utf-8 -*-

# 项目目录指定扩展名文件的个数
# projectDir指向项目目录，注意必须包含结尾的/


import glob
from subprocess import check_output
import os


def stat(projectDir: str) -> dict:

    # projectDir = "/Users/harley/Downloads/ExampleCLI-master/"
    # projectDir = "/Users/harley/Downloads/cdp-projects/"

    if not projectDir.endswith("/"):
        projectDir = projectDir + "/"

    extensions = [".swift", ".java", ".js", ".ts"]
    extFileCounts = {}
    for ext in extensions:
        extFileCounts[ext] = 0

    ignoreDirs = ['node_modules', '.git']
    for filename in glob.iglob(projectDir + "**/*", recursive=True):
        if len(ignoreDirs) > 0:
            for ignore in ignoreDirs:
                if filename.find(ignore) > 0:
                    continue

        _, ext = os.path.splitext(filename)
        if ext in extensions:
            extFileCounts[ext] = extFileCounts[ext] + 1

    return extFileCounts


lineCount = 0
projectsDir = "/Users/harley/Downloads/vue-2.6.11"

projectsDir = "/Users/harley/Downloads/vue-2.6.11"
for entry in os.listdir(projectsDir):
    fullPath = os.path.join(projectsDir, entry)
    if os.path.isdir(fullPath):
        result = stat(fullPath)
        print("======== %s =========" % entry)
        for k, v in result.items():
            print("%s : %d" % (k, v))


