# -*- coding: utf-8 -*-
# coding=utf-8
import sys
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
# env.hosts = ["hk330"]


def push(loc, remote):
    put(loc, remote)


class envs(object):

    @property
    def debug(self):
        return "/var/www/pine"

    @property
    def release(self):
        return "/home/www/pine/mysite"

    def path(self, isDebug=True):
        print green(isDebug)
        return isDebug is True and self.debug or self.release


envs = envs()


@hosts("hk330", )
def publish(debug=True):
    """
    pull the lasted to the project
    :param debug: env
    :return: None
    """
    pa = envs.path(debug)
    with cd(pa):
        print green("Refresh beginning ...")
        run("git fetch")
        branch = "%s" % (debug is True and "dev" or "master")
        run("git checkout %s" % branch)

        fb = StringIO()
        get("%s/%s" % (pa, "version.txt"), fb)
        old = fb.getvalue()
        fb.close()
        ver = run("git rev-parse HEAD")
        if not old or ver != old:
            print red("old version:%s" % old)
            print red("new version:%s" % ver)
            # with prefix("git"):
            run("git pull origin %s" % branch)
            print green("Refresh complete.")
            run("git rev-parse HEAD > %s" % "version.txt")
            run("python manage.py makemigrations")
            run("python manage.py migrate")
            run("python manage.py collectstatic")
        fb.close()


@hosts("hk330", )
def deploy(debug=True):
    """
    restart the nginx and others.
    :param debug: env
    :return: None
    """
    pa = envs.path(debug)
    with cd(pa):
        print green("Publish is beginning ...")
        uwsgi = "%s/%s" % (pa, "uwsgi.ini")
        pids = run("ps -auxf | grep \'%s\' | awk \'{print $2}\'" % uwsgi).replace('\r\n', '\n').split('\n')
        for pid in pids:
            sudo("kill -s 9 %s" % pid)
        # sudo("killall -9 uwsgi")
        sudo("uwsgi %s" % uwsgi)
        sudo("service nginx restart")
        print green("Publish is complete.")


@hosts("hk330", )
def task(debug=True):
    execute(publish, debug)
    execute(deploy, debug)


@hosts("hk330", )
def restart():
    print red("Reboot will be restart after 5s ...")
    reboot(wait=5)
    print red("Reboot has been restart...")


if __name__ == "__main__":
    task(True)
