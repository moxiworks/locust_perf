import json
from faker import Faker
from locust import HttpUser, task, between
from data import (dedupe_params,dedupe_endpoint, auth,
                  headers)

class PerfListingSvc(HttpUser):
    def __init__(self, parent):
        super(PerfListingSvc, self).__init__(parent)
        self.dedupe_endpoint = dedupe_endpoint
        self.dedupe_params = dedupe_params
        self.auth = auth
        self.headers = headers
        self.mock = Faker()

    @task()
    def get_dedupe_V1(self):
        try:
            resp = self.client.get(url=self.dedupe_endpoint, params={**self.dedupe_params, **self.auth})
            assert resp.status_code == 200
        except Exception as e:
            print("request_failed", e)

