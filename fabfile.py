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


@property
def debug():
    return '/var/www/pine'


@property
def release():
    return '/home/www/pine/mysite'


def path(isDebug=True):
    if isDebug:
        return debug
    else:
        return release


@hosts('hk330', )
def publish(debug=True):
    """
    pull the lasted to the project
    :param debug: env
    :return: None
    """
    with cd(path(debug)):
        print green('Refresh beginning ...')
        fb = StringIO()
        get('%s/%s' % (path, "version.txt"), fb)
        old = fb.getvalue()
        ver = run('git rev-parse HEAD')
        if not old or ver != old:
            print red('old version:%s' % old)
            print red('new version:%s' % ver)
            # with prefix('git'):
            run('git fetch')
            branch = '%s' % (debug and 'dev' or 'master')
            run('git checkout %s' % branch)
            run('git pull origin %s' % branch)
            print green('Refresh complete.')
            fb.write(ver)
            fb.flush()
            run('python manage.py makemigrations')
            run('python manage.py migrate')
            run('python manage.py collectstatic')
        fb.close()


@hosts('hk330', )
def deploy(debug=True):
    """
    restart the nginx and others.
    :param debug: env
    :return: None
    """
    with cd(path(debug)):
        print green('Publish is beginning ...')
        uwsgi = '%s/%s' % (path(debug), 'uwsgi')
        pids = run('ps -auxf | grep \'%s\' | awk \'{print $2}\'' % uwsgi).replace('\r\n',
                                                                                  '\n').split('\n')
        for pid in pids:
            sudo('kill -s 9 %s' % pid)
        # sudo('killall -9 uwsgi')
        sudo('uwsgi %s' % uwsgi)
        sudo('service nginx restart')
        print green('Publish is complete.')


@hosts('hk330', )
def task(debug=True):
    execute(publish, debug)
    execute(deploy, debug)


@hosts('hk330', )
def restart():
    print red('Reboot will be restart after 5s ...')
    reboot(wait=5)
    print red('Reboot has been restart...')
