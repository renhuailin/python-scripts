#!/usr/bin/env python3
from pexpect import *
import pexpect
import os
import sys
import argparse

PROMPT = ['# ', '>>> ', '> ', '\$ ']


def send_command(child, cmd):
    child.sendline(cmd)
    child.expect(PROMPT)
    # print(child.before)
    child.send('\n')
    child.interact()


def get_password_from_keychain(host: str, account: str):
    cmd = ' '.join([
        "/usr/bin/security",
        " find-generic-password",
        "-w -s '%s' -a '%s'" % (host, account)
    ])

    # print(cmd)
    p = os.popen(cmd)
    output = p.read()
    exit_code = p.close()
    # print("exit code : %d", exit_code)
    if exit_code is not None:
        # print(output)
        return None

    return output


def connect(host: str, port: int, user: str, password: str):
    ssh_newkey = 'Are you sure you want to continue connecting'

    connStr = 'ssh ' + user + '@' + host
    connStr = "ssh -p %d  %s@%s" % (port, user, host)

    child = pexpect.spawn(connStr)
    ret = child.expect([pexpect.TIMEOUT, ssh_newkey,
                        '[P|p]assword:'])

    if ret == 0:
        print('[-] Error Connecting')
        return

    if ret == 1:
        child.sendline('yes')
        ret = child.expect([pexpect.TIMEOUT,
                            '[P|p]assword:'])
        if ret == 0:
            print('[-] Error Connecting')
            return

    child.sendline(password)
    child.expect(PROMPT)
    return child


def main(host: str, port: int, user: str):
    # host = '10.218.128.38'
    # user = 'ubuntu'
    # password = 'faw_vw@018'

    password = get_password_from_keychain(host, user)
    if password == None:
        print("The specified item could not  be found in the keychain.")
        exit(44)

    child = connect(host, port, user, password)
    send_command(child, 'cd ~')


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--server", help="ssh server , name or ip")
    parser.add_argument("-p", "--port", help="ssh port")
    parser.add_argument("-u", "--username", help="username")
    args = parser.parse_args()

    if args.server:
        host = args.server
    else:
        print("fdsfdsfsd")
        exit(-1)
    
    if args.username:
        username = args.username
    else:
        username = "root"

    if args.port:
        port = args.port
    else:
        port = "22"

    

    # print(sys.argv)
    # print(' '.join(sys.argv[1:]))

    main(host, int(port), username)
