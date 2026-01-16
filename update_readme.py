import requests
from datetime import datetime

def update_readme():
    try:
        # Fetch repositories
        api_url = "https://api.github.com/users/cedrickcuencaalegsao/repos?sort=pushed&per_page=100"
        response = requests.get(api_url)
        response.raise_for_status()
        
        # Filter and get top 5 non-forked repos
        repos = [repo for repo in response.json() if not repo['fork']][:5]
        
        # Generate project content
        projects_content = ""
        for repo in repos:
            desc = repo['description'] or "No description available"
            projects_content += f"- 🚀 **[{repo['name']}]({repo['html_url']})**\n"
            projects_content += f"  - {desc}\n"
            projects_content += f"  - ⭐ {repo['stargazers_count']} stars | 🔄 Last updated: {repo['updated_at'][:10]}\n\n"
        
        # Update README
        with open('README.md', 'r', encoding='utf-8') as file:
            content = file.read()
        
        start_marker = '<!-- PROJECTS_START -->'
        end_marker = '<!-- PROJECTS_END -->'
        
        start_idx = content.find(start_marker)
        end_idx = content.find(end_marker)
        
        if start_idx != -1 and end_idx != -1:
            new_content = (
                content[:start_idx + len(start_marker)] +
                f"\n{projects_content}" +
                content[end_idx:]
            )
            
            with open('README.md', 'w', encoding='utf-8') as file:
                file.write(new_content)
            
            print("✅ README updated successfully!")
        else:
            print("❌ Could not find project markers in README")
            
    except Exception as e:
        print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    update_readme()