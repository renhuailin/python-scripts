import os
from os import listdir
import os.path as path
import shutil

# 用mvn来批量生成java项目的文档，并统一输出到一个目录(如nginx的html目录)。

# 这是源代码所在目录
localFolder = "/Users/harley/Documents/Workspace/java/IBM"

# javadoc输出目录，如nginx或apache的html目录。
outputDir = "/Users/harley/Documents/tmp/javadocs"

dirs = [path.join(localFolder, f)
        for f in listdir(localFolder) if not f.startswith(".") and path.isdir(path.join(localFolder, f))]


if not shutil.which("mvn"):
    print("please intall mvn first.")
    exit(-1)


for dir in dirs:
    cmd = "cd %s && mvn javadoc:javadoc" % (dir,)
    print(cmd)
    os.system(cmd)


for dirpath, dirnames, filenames in os.walk("."):
    if dirpath.endswith("site/apidocs"):
        print(dirpath)
        i = dirpath.index("/target/site/apidocs")
        projectDir = dirpath[2:i]
        print(projectDir)
        print(os.path.join(outputDir, projectDir))

        destDir = os.path.join(outputDir, projectDir)
        if os.path.exists(destDir):
            shutil.rmtree(destDir)

        shutil.copytree(dirpath, destDir)

        for filename in [f for f in filenames if f.endswith("index.html")]:
            print(os.path.join(dirpath, filename))
