import json
from faker import Faker
from random import randrange
from locust import HttpUser, task
from data import (alt_off_ag_uuids,v2_endpoint, auth,
                  headers)

class PerfProfileSvc(HttpUser):
    def __init__(self, parent):
        super(PerfProfileSvc, self).__init__(parent)
        self.v2_endpoint = v2_endpoint
        self.alt_off_ag_uuids = alt_off_ag_uuids
        self.auth = auth
        self.headers = headers
        self.mock = Faker()

    @task()
    def get_v2_insec_comp_ag(self):
        rand_uuid = randrange(len(self.alt_off_ag_uuids))
        try:
            resp = self.client.get(url=f"{self.v2_endpoint}{self.alt_off_ag_uuids[rand_uuid]}", params=self.auth)
            assert resp.status_code == 200
        except Exception as e:
            print("request_failed", e)

