import os
from time import *
from os import path
from git import Repo

from github import Github
from dotenv import load_dotenv

load_dotenv()
access_token = os.environ.get("access_token")

print(access_token)