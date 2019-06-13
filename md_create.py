import os
import subprocess
from traverse_readme import traverseReposAndGetRequiredReading
import time

path_folder = "/Users/Christian/Desktop/Python Mandatory/Reading Repo" 
remote_repo_url = "https://github.com/Skydt90/Python_required_reading.git"

# creates a local md file, based on list returned by traverse_readme module
def createMDFile(required_reading_list):
    file_name = "required_reading"

    # opens a new file by joining pathfolder with filename using .format
    with open(os.path.join(path_folder, "{}.md".format(file_name)), mode = "w") as md_file:
        md_file.write("# Required Reading \n  > Python Elective I Spring 2019\n")   # write boilerplate headers
        
        for line in required_reading_list:                                          # for every line i list
            md_file.write(line + "\n")                                              # write to file and append \n

# pulls remote md repo, calls createMDfile and pushes file to github
def pullAndPushToGit():
    os.chdir(path_folder)                                                           # change path to local git repo
    
    cmd = "git reset HEAD --hard"                                                   # reset local hard
    subprocess.Popen(cmd, shell = True)                                             # execute
    cmd = "git pull " + remote_repo_url + " --allow-unrelated-histories"            # pull remote
    subprocess.Popen(cmd, shell = True)                                             # execute
    time.sleep(2)                                                                   # sleep to stop overlap in commit

    createMDFile(traverseReposAndGetRequiredReading())                              # create the new md file

    subprocess.call("git add .", shell = True)                                      # add file
    subprocess.call("git commit -m 'Reading File Commit'", shell = True)            # commit file
    subprocess.call("git push origin master", shell = True)                         # push to remote