import json
import requests
import subprocess
import os

base_path = "/Users/Christian/Desktop/Python Mandatory/Repositories/"
API_URL = "https://api.github.com/orgs/python-elective-1-spring-2019/repos?per_page=100"
HEADER = {"content-type": "application/json"}

# calls api and returns a json list response
def getGithubCloneUrls():
    response = requests.get(API_URL, HEADER)                           # calls the api using url and header
    if response.status_code == 200:                                    # if success
        return extractJsonToDict(json.loads(response.content))         # execute remaining program 
    else:
        return None

# return dict with name + clone url from json response
def extractJsonToDict(content):
    dict = {}
    for entry in content:                                              # loops every entry in json response list
        link = entry["clone_url"]                                      # link = entry after "clone_url"
        name = entry["name"]                                           # name = entry after "name"
        dict[name] = link                                              # dict key = name, value = link   
    return dict

# clones and pulls remote repos to local
def cloneAndPullRepos(url_dict):
    os.chdir(base_path)                                                # change path to local repo store directory

    for (name, url) in url_dict.items():                               # for each k, v in dict
        if not os.path.exists(base_path + name):                       # if path does not exist
            cmd = "git clone " + url
            subprocess.Popen(cmd, shell = True)                        # clone remote repo to local
        else:
            os.chdir(base_path + name)                                 # else change path to local repo
            cmd = "git pull " + url + " --allow-unrelated-histories"
            subprocess.Popen(cmd, shell = True)                        # pull the repo
            os.chdir(base_path)                                        # change path back to working directory