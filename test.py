import requests

r = requests.get('https://stan-izone.firebaseio.com/users.json')

print(r.json())

