import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        pass

    def load_json(self):
        pass

    def get_response_body(self):
        pass
        URL = 'https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json'
        response = requests.get(URL)
        return response.content

    def load_json(self):
        pass
        people = json.loads(self.get_response_body())
        return people