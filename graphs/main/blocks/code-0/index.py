import os
import re
import requests

def token():
  file_path = os.path.abspath(os.path.join(__file__, "../../../../token.txt"))
  with open(file_path, "r") as file:
    content = file.read()
    content = re.sub(r"[\s\n]+", "", content)
  return content

def main(props, context):
  response = requests.get(
    "https://api.github.com/repos/flows-example/github-project-migrator/projects", 
    headers={
      "Accept": "application/vnd.github+json",
      "Authorization": f"Bearer {token()}",
      "X-GitHub-Api-Version": "2022-11-28",
    },
  )
  if response.status_code != 200:
    print(response.content)
    raise Exception(f"status {response.status_code}")
  
  context.result(response.json(), "out", True)
