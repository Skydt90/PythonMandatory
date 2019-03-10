import sys
import time
from request_clone_and_pull import cloneAndPullRepos, getGithubCloneUrls
from md_create import createMDFile, pullAndPushToGit

def main():
    cloneAndPullRepos(getGithubCloneUrls())
    time.sleep(3)
    pullAndPushToGit()

if __name__ == "__main__":
    main()