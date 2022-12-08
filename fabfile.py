from fabric.api import env, local, cd, run, prefix

env.hosts = ['sdelquin.me']


def deploy():
    local('git push')
    with prefix('source ~/.pyenv/versions/names/bin/activate'):
        with cd('~/code/names'):
            run('git pull')
            run('pip install -r requirements.txt')
            run('supervisorctl restart names')
