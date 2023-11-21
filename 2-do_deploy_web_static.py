#!/usr/bin/python3
"""
Fabric script based on the file 1-pack_web_static.py that distributes an
archive to the web servers
"""

from fabric import Connection, task
from os.path import exists

env = {
    "hosts": ['35.153.18.226', '100.26.244.69'],
    "user": 'ubuntu',
    "key_filename": '~/.ssh/school'
}

@task
def do_deploy(c, archive_path):
    """distributes an archive to the web servers"""
    if exists(archive_path) is False:
        return False
    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        c.put(archive_path, '/tmp/')
        c.run('mkdir -p {}{}/'.format(path, no_ext))
        c.run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))
        c.run('rm /tmp/{}'.format(file_n))
        c.run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        c.run('rm -rf {}{}/web_static'.format(path, no_ext))
        c.run('rm -rf /data/web_static/current')
        c.run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False
