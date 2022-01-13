import git
import datetime
import os
from time import *
from os import path
from git import Repo

# access_token = "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"

# g = git(access_token)
# repo = g.get_repo("GET", "https://api.github.com/repos/zeze1004/AWS_K8s/pulls")

def commit_files():
    curr_dir = os.path.dirname(os.path.realpath(__file__))
    repo = Repo(curr_dir)
    local_repo_path = "."
    if repo != None:
        new_branch = 'feature/new_branch_test'
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