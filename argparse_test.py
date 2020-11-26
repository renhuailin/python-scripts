# -*- coding: utf-8 -*-
import argparse
import os

parser = argparse.ArgumentParser()
# parser.add_argument("exchange", help="name of an exchange")
parser.add_argument("-u", "--user", help="mysql username")
parser.add_argument("-p", "--password", help="mysql password")
parser.add_argument("-t", "--host", help="mysql host")
parser.add_argument("-d", "--database", help="mysql database name")
parser.add_argument("-r", "--redis", help="redis host")
parser.add_argument("-rd", "--redis_database", help="redis database")
parser.add_argument("-rp", "--redispassword", help="redis password")
args = parser.parse_args()

if args.user:
    mysql_user = args.user
else:
    print("please input user name")
    parser.print_help()
    exit(-1)

    mysql_user = os.environ.get('MYSQL_USER', "root")

if args.password:
    mysql_password = args.password
else:
    mysql_password = os.environ.get('MYSQL_PASSWORD', "mysql")

if args.host:
    mysql_host = args.host
else:
    mysql_host = os.environ.get('MYSQL_HOST', "127.0.0.1")

if args.database:
    mysql_database = args.database
else:
    mysql_database = os.environ.get('MYSQL_DATABASE', "crypto_currency")

if args.redis:
    redis_host = args.redis
else:
    redis_host = os.environ.get('REDIS_HOST', "127.0.0.1")

if args.redispassword:
    redis_password = args.redispassword
else:
    redis_password = os.environ.get('REDIS_PASSWORD', "")

if args.redis_database:
    redis_database = args.redis_database
else:
    redis_database = os.environ.get('REDIS_DATABASE', "0")

# print("Trader for exchange %s" % args.exchange)
print(
    "mysql host: %s database: %s user: %s password: %s " % (mysql_host, mysql_database, mysql_user, mysql_password))
print("redis host: %s password: %s " % (redis_host, redis_password))
    
if __name__ == '__main__':
    print("fsdafsdfsd")
    