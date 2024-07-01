from faker import Faker
from locust import HttpUser, task
from data import (groups_endpoint, groups_search_endpoint,  groups_params, headers)


class PerfProfileSvc(HttpUser):
    def __init__(self, parent):
        super(PerfProfileSvc, self).__init__(parent)
        self.groups_endpoint = groups_endpoint
        self.groups_search_endpoint = groups_search_endpoint
        self.groups_params = groups_params
        self.headers = headers
        self.mock = Faker()

    @task()
    def get_groups(self):
        try:
            resp = self.client.get(url=self.groups_endpoint,
                                   params=self.groups_params, headers=self.headers)
            assert resp.status_code == 200
        except Exception as e:
            print("request_failed", e)
            print(resp.json())

    @task()
    def search_groups(self):
        try:
            resp = self.client.get(url=self.groups_search_endpoint,
                                   params=self.groups_params, headers=self.headers)
            assert resp.status_code == 200
        except Exception as e:
            print("request_failed", e)
            print(resp.json())


