from fabric.api import env, local, prefix, cd, run

env.hosts = ["production"]


def deploy():
    local("git push")
    with prefix("source ~/.virtualenvs/names/bin/activate"):
        with cd("~/names"):
            run("git pull")
            run("pip install -r requirements.txt")
            run("supctl restart names")
