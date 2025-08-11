with open('requirements.txt', 'r') as myfile:
    data = [req.replace('\n','')  for req in myfile.readlines() if '-e' not in req]

print(data)