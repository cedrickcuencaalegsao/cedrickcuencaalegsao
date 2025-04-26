import requests
from datetime import datetime

# Fetch pinned repositories
api_url = "https://api.github.com/users/cedrickcuencaalegsao/repos?sort=pushed"
response = requests.get(api_url)
repos = response.json()[:3]  # Get 3 newest repos

projects_content = "".join(
    f"- 🚀 **{repo['name']}**\n  - {repo['description']}\n"
    for repo in repos if not repo['fork']
)

# Update README
with open('README.md', 'r') as file:
    content = file.read()

new_content = content.replace(
    '<!-- PROJECTS_START -->\n<!-- PROJECTS_END -->',
    f'<!-- PROJECTS_START -->\n{projects_content}\n<!-- PROJECTS_END -->'
)

with open('README.md', 'w') as file:
    file.write(new_content)