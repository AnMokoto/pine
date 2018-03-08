# -*- coding: utf-8 -*-
# coding=utf-8
from fabric.api import (
    cd, lcd, run, local, sudo, put, get,

    execute, reboot, env, prefix, parallel, hosts
)
from fabric.colors import *
from StringIO import StringIO

env.warn_only = True
env.use_ssh_config = True


# 任务并行
# env.parallel = True
# env.hosts = ['hk330']


def push(loc, remote):
    put(loc, remote)


@hosts('hk330', )
def publish(path='/home/www/pine/mysite'):
    """
    pull the lasted to the project
    :param path: project path at remote server
    :return: None
    """
    with cd(path):
        print green('Refresh beginning ...')
        fb = StringIO()
        get(path + "/version.txt", fb)
        old = fb.getvalue()
        ver = run('git rev-parse HEAD')
        if not old or ver != old:
            print red('old version:%s' % old)
            print red('new version:%s' % ver)
            # with prefix('git'):
            run('git fetch')
            run('git pull origin master')
            print green('Refresh complete.')
            fb.write(ver)
            fb.flush()
            run('python manager.py makemigrations')
            run('python manager.py migrate')
            run('python manager.py collectstatic')
        fb.close()


@hosts('hk330', )
def deploy(path='/home/www/pine/mysite'):
    """
    restart the nginx and others.
    :param path: project path at remote server
    :return: None
    """
    with cd(path):
        print green('Publish is beginning ...')
        sudo('killall -9 uwsgi')
        sudo('uwsgi uwsgi.ini')
        sudo('service nginx restart')
        print green('Publish is complete.')


@hosts('hk330', )
def task(path='/home/www/pine/mysite'):
    execute(publish, path)
    execute(deploy, path)


@hosts('hk330', )
def restart():
    print red('Reboot will be restart after 10s ...')
    reboot(wait=10)
    print red('Reboot has been restart...')
