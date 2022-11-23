import requests


class Externals:
    def external(self, resource="http://127.0.0.1:3001/users"):
        response = requests.get(resource)
        print(response.json())


user = Externals()
user.external()
