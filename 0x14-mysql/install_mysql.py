#!/usr/bin/python3
"""Install version 5.7.x of mysql"""
from fabric.api import *


env.user = 'ubuntu'
#env.hosts = ['35.231.116.248', '54.83.93.155']

def do_first_steps():
    run('mysql -uroot -p -e "CREATE USER IF NOT EXISTS holberton_user@localhost IDENTIFIED BY \'projectcorrection280hbtn\';"')
    run('mysql -uroot -p -e "GRANT REPLICATION CLIENT ON *.* TO \'holberton_user\'@\'localhost\';"')
    run("sudo echo 'deb http://repo.mysql.com/apt/ubuntu/ trusty mysql-5.7-dmr' | sudo tee -a /etc/apt/sources.list")
    run('sudo apt-get update')
    run('sudo apt-get install mysql-server-5.7')
    run('mysql --version')
    run('mysql -uroot -p -e "CREATE DATABASE IF NOT EXISTS tyrell_corp;"')

def do_master():
    run('mysql -uroot -p -e "CREATE DATABASE IF NOT EXISTS tyrell_corp;"')
    run('mysql -uroot -p -e "CREATE TABLE IF NOT EXISTS tyrell_corp.nexus6 (id INT, name varchar(30));"')
    run('mysql -uroot -p -e "GRANT SELECT ON tyrell_corp.* TO \'holberton_user\'@\'localhost\';"')
    run('mysql -uroot -p -e "CREATE USER IF NOT EXISTS replica_user@\'%\' IDENTIFIED BY \'replica_user\';"')
    run('mysql -uroot -p -e "GRANT REPLICATION SLAVE ON *.* TO \'replica_user\'@\'%\";"')
    run('mysql -uroot -p -e "GRANT SELECT ON mysql.user TO \'holberton_user\'@\'localhost\';"')

def do_slave():
    pass
