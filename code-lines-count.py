#! /usr/bin/python3


# 统计代码行数
# projectDir指向项目目录，注意必须包含结尾的/


import glob
from subprocess import check_output
import os


def soureCodeLineCount(filename: str):
    # int(output)
    # output = check_output("cat %s |wc -l" %
    #                       filename, encoding="UTF-8", shell=True)
    # print(int(output))

    num_lines = sum(1 for line in open(filename))
    return int(num_lines)


def calculate(projectDir: str) -> int:

    # projectDir = "/Users/harley/Downloads/ExampleCLI-master/"
    # projectDir = "/Users/harley/Downloads/cdp-projects/"

    if not projectDir.endswith("/"):
        projectDir = projectDir + "/"

    extensions = [".swift", ".java", ".js", ".ts"]

    totalLineCount = 0

    ignoreDirs = ['node_modules', '.git']
    for filename in glob.iglob(projectDir + "**/*", recursive=True):
        if len(ignoreDirs) > 0:
            for ignore in ignoreDirs:
                if filename.find(ignore) > 0:
                    continue

        f, ext = os.path.splitext(filename)
        # print(ext)
        if ext in extensions:
            count = soureCodeLineCount(filename)
            # print('%s - %d' % (filename, count))
            totalLineCount = totalLineCount + count

    print("project: %s - total lines: %d" % (projectDir, totalLineCount))
    return totalLineCount


lineCount = 0
projectsDir = "/Users/harley/Downloads/vue-2.6.11"
for entry in os.listdir(projectsDir):
    fullPath = os.path.join(projectsDir, entry)
    if os.path.isdir(fullPath):
        # print('d-%s' % fullPath)
        lineCount = lineCount + calculate(fullPath)

print("All projects total lines: %d" % lineCount)
