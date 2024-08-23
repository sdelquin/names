from fabric.api import cd, env, local, prefix, run

env.hosts = ['sdelquin.me']


def deploy():
    local('git push')
    with prefix('source .venv/bin/activate'):
        with cd('~/code/names'):
            run('git pull')
            run('pip install -r requirements.txt')
            run('supervisorctl restart names')
