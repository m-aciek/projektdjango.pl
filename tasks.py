from invoke import task
from settings import DEPLOY_TARGET


@task
def deploy(c):
    command = 'rsync {extraargs} -avz index.html static {target}'
    c.run(command.format(extraargs='--dry-run', target=DEPLOY_TARGET))
    if input('Are you sure you want to deploy?') == 'yes':
        c.run(command.format(extraargs='', target=DEPLOY_TARGET))
