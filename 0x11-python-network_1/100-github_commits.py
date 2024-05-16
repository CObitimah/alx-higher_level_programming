#!/usr/bin/python3
"""
This script takes a repository name and owner name as arguments.
"""

import sys
import requests


def get_commits(repo, owner):
    url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    response = requests.get(url)
    if response.status_code == 200:
        commits = response.json()[:10]  # Get the first 10 commits
        for commit in commits:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    else:
        print("Error fetching commits")


if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    get_commits(repo_name, owner_name)
