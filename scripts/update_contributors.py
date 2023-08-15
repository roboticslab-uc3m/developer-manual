# pre-requisites: pip install PyGithub PyYAML

import os
import textwrap
import yaml

from datetime import datetime

from github import Github, Auth
from github.GithubException import IncompletableObject

ALIASES_FILE = 'dev-aliases.yaml'
OUT_FILE = 'contributors.md'
ORG_NAME = 'roboticslab-uc3m'

with open(ALIASES_FILE, 'r', encoding='utf-8') as f:
    aliases = yaml.safe_load(f)

# required fine-grained PAT permissions:
# * repository permissions: metadata (read-only)
# * organization permissions: administration (read-only)
# also make sure to check the 'All repositories' checkbox
auth = Auth.Token(os.environ.get('GITHUB_PAT_AUTH'))

g = Github(auth=auth)
org = g.get_organization(ORG_NAME)

print(f'public repositories: {org.public_repos}')
print(f'private repositories: {org.total_private_repos}')

repos = [repo for repo in org.get_repos() if not repo.fork]
print(f'retrieved {len(repos)} target repositories')

registered = {}
anons = {}

for count, repo in enumerate(repos, start=1):
    for contributor in repo.get_contributors(anon=True):
        if contributor.type == 'Bot':
            continue

        try:
            registered[contributor.name or contributor.login] = contributor.login
        except IncompletableObject as e:
            anons[aliases.get(contributor.name, contributor.name)] = None # anons

    print(f'({count}/{len(repos)}) {repo.name}')

anons = {k: v for k, v in anons.items() if k not in registered.values()} # ignore known GitHub nicknames
anons.update(registered) # overlapping items are overwritten by registered_users

sorted = dict(sorted(anons.items(), key=lambda i: i[0].casefold())) # ignore case

with open(OUT_FILE, 'w', encoding='utf-8') as f:
    f.write(textwrap.dedent(f"""\
        # Contributors

        This is a list of people who contributed to the {ORG_NAME} software ecosystem.
        Generated on {datetime.today().strftime('%Y-%m-%d')}.

        """))

    for proper_name, github_name in sorted.items():
        if github_name is not None and github_name != proper_name:
            f.write(f'- {proper_name} ({github_name})\n')
        else:
            f.write(f'- {proper_name}\n')
