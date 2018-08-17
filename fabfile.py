from fabric.api import env, local, cd, run

env.hosts = ['production']


def deploy():
    local('git push')
    with cd('~/names'):
        run('git pull')
        run('pipenv install')
        run('supctl restart names')
