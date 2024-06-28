from faker import Faker
from locust import HttpUser, task
from data import (syndication_office_endpoint, syndication_office_search_endpoint, syndication_office_params, auth, headers)


class PerfProfileSvc(HttpUser):
    def __init__(self, parent):
        super(PerfProfileSvc, self).__init__(parent)
        self.syndication_office_endpoint = syndication_office_endpoint
        self.syndication_office_search_endpoint = syndication_office_search_endpoint
        self.syndication_office_params = syndication_office_params
        self.auth = auth
        self.headers = headers
        self.mock = Faker()

    @task()
    def get_synd_office(self):
        try:
            resp = self.client.get(url=self.syndication_office_endpoint,
                                   params={**self.syndication_office_params, **self.auth})
            assert resp.status_code == 200
        except Exception as e:
            print("request_failed", e)

    @task()
    def get_synd_office_search(self):
        try:
            resp = self.client.get(url=self.syndication_office_search_endpoint,
                                   params={**self.syndication_office_params, **self.auth})
            assert resp.status_code == 200
        except Exception as e:
            print("request_failed", e)
