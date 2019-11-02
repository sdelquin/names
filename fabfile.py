from fabric.api import env, local, cd, run

env.hosts = ['cloud']


def deploy():
    local('git push')
    with cd('~/names'):
        run('git pull')
        run('pipenv install')
        run('supervisorctl restart names')
