from invoke import task
from settings import DEPLOY_TARGET


@task
def deploy(c):
    c.run(f'rsync --dry-run -avz index.html {DEPLOY_TARGET}')
    if input('Are you sure you want to deploy?') == 'yes':
        c.run(f'rsync -avz index.html {DEPLOY_TARGET}')
