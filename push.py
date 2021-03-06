import git
import datetime
import os
from time import *
from os import path
from git import Repo

from github import Github
from dotenv import load_dotenv

load_dotenv()
access_token = os.environ.get("access_token")

g = Github(access_token)

repo = g.get_repo("zeze1004/githubapi")



# def git_pull_repo(repo, directory) {
#     # terraform-env-alpha, ~/project/terraform-env-alpha
#     # 1. pull 받는다.
# }

# def git_commit_and_push(repo, directory) {
#    '''
#             repo.git.add(A=True)
#             repo.git.commit(m='msg')
#             repo.git.push('--set-upstream', 'origin', current)
#             print('git push')
#    ''' 
# }

# def create_github_pr(repo, directory, title, body, local_branch, origin_branch) {
# }

# def create_test_diff() {
#          #creating file
#         dtime = strftime('%d-%m-%Y %H:%M:%S', localtime())
#         with open(local_repo_path + path.sep + 'lastCommit' + '.txt', 'w') as f:
#             f.write(str(dtime))
#         if not path.exists(local_repo_path):
#             os.makedirs(local_repo_path)   
# }

# git_pull_repo
# create_test_diff()
# git_commit_and_push
# create_github_pr()

def commit_files():
    curr_dir = os.path.dirname(os.path.realpath(__file__))
    repo = Repo(curr_dir)
    local_repo_path = "."
    
    if repo != None:
        new_branch = 'feature/new_branch_test1'
        current = repo.create_head(new_branch)
        current.checkout()
        main = repo.heads.main
        repo.git.pull('origin', main)
        #creating file
        dtime = strftime('%d-%m-%Y %H:%M:%S', localtime())
        with open(local_repo_path + path.sep + 'lastCommit' + '.txt', 'w') as f:
            f.write(str(dtime))
        if not path.exists(local_repo_path):
            os.makedirs(local_repo_path)
        print('file created---------------------')

        if repo.index.diff(None) or repo.untracked_files:

            repo.git.add(A=True)
            repo.git.commit(m='msg')
            repo.git.push('--set-upstream', 'origin', current)
            print('git push')
        else:
            print('no changes')


commit_files()
repo.create_pull('PR title', 'Body', head="feature/new_branch_test1", base="main")