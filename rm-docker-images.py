# -*- coding: utf-8 -*-

from subprocess import check_output, CalledProcessError
from io import StringIO


def rm_docker_images(matchFilter):
    output = check_output("docker images", encoding='UTF-8', shell=True)
    s = StringIO(output)
    for line in s:
        print(line)
        info = line.split()
        # print info[2]
        name = info[0]
        version = info[1]
        image_id = info[2]
        if matchFilter(name, version):
            delete_docker_image_by_hash(image_id)
            # delete_docker_image_by_version(name,version)

        # call(["docker", 'inspect', info[2]])


def delete_docker_image_by_hash(hash):
    # call(["docker", 'rmi', hash])
    try:
        output = check_output(["docker", 'rmi', '-f', hash])
        print(output)
    except CalledProcessError:
        pass


def delete_docker_image_by_version(name, version):
    # call(["docker", 'rmi', hash])
    try:
        output = check_output(["docker", 'rmi', '-f', "%s:%s" % (name, version)])
        print(output)
    except CalledProcessError:
        pass


def filter(name, version):
    print("name: %s version: %s" % (name, version))
    if name == '<none>':
        return True

    if version == '<none>':
        return True

    if name.startswith("registry.xiangcloud.com.cn"):
        return True

    return False


if __name__ == "__main__":
    rm_docker_images(filter)
