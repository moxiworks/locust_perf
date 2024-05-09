import json
from faker import Faker
from locust import HttpUser, task
from data import (insec_comp_ag_params,v2_insec_comp_ag_endpoint, auth,
                  headers)

class PerfProfileSvc(HttpUser):
    def __init__(self, parent):
        super(PerfProfileSvc, self).__init__(parent)
        self.v2_insec_comp_ag_endpoint = v2_insec_comp_ag_endpoint
        self.insec_comp_ag_params = insec_comp_ag_params
        self.auth = auth
        self.headers = headers
        self.mock = Faker()

    @task()
    def get_v2_insec_comp_ag(self):
        try:
            resp = self.client.get(url=self.v2_insec_comp_ag_endpoint, params={**self.insec_comp_ag_params, **self.auth})
            assert resp.status_code == 200
        except Exception as e:
            print("request_failed", e)

