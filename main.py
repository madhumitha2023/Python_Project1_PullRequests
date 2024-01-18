#This code is written to get the user names of the pull requests made to Git hub repo

import requests

#To get the pull requests URL, Browse for "GitHub REST API documentation - GitHub Docs" in google and click on REST API and enter Pulls 

response = requests.get("http://api.github.com/repos/kubernetes/kubernetes/pulls")

for i in range(len(response.json())):
    print(response.json()[i]["user"]["login"])