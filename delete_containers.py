# -*- coding: utf-8 -*-

import StringIO
from subprocess import call, check_output, CalledProcessError

ids = """e92c5e598590
b15c70f53dfc
c9078612aa06
5cac9a5dbdc7
c72d122a5785
86036076a1b8
32e3201482bd
0098885a0645
87ba88e92730
60f28085326c
40d87774600f
b4ff373df202
e2983501894a
8fcbc3ed0733
d1df4bcae166
533b67b42c81
7af88c127a65"""


# output = check_output(["docker", 'ps','-a'])
# print output

for id in StringIO.StringIO(ids):

    # print id
    try:
        print "docker rm %s " % id
        # call(["docker", 'rm', id])
        # output = check_output(["docker", 'inspect', id])
        # output = check_output(["docker", 'rm', id])
        # print "output: &s " % output
    except CalledProcessError:
        pass
