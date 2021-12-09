import json
from faker import Faker
from locust import HttpUser, task, between
from data import (upsert_endpoint,
                  create_endpoint,
                  auth,
                  create_params,
                  upsert_params,
                  additional_params,
                  headers)

class PerfCrmSvc(HttpUser):

    def __init__(self, parent):
        super(PerfCrmSvc, self).__init__(parent)
        self.upsert_endpoint = upsert_endpoint
        self.upsert_params = upsert_params
        self.auth = auth
        self.headers = headers
        self.create_endpoint = create_endpoint
        self.create_params = create_params
        self.additional_params = additional_params
        self.mock = Faker()

    @task()
    def create_contacts(self):

        self.create_params["given_name"] = self.mock.first_name()
        self.create_params["middle_name"] = self.mock.first_name()
        self.create_params["surname"] = self.mock.last_name()
        self.create_params["email_addresses"][0]["text"] = self.mock.email()

        resp = self.client.post(url=self.create_endpoint, json=self.create_params, params=self.auth)
        assert resp.status_code == 201

    @task()
    def upsert_contacts(self):

        self.upsert_params["user_uuid"] = self.mock.uuid4()
        data = {**self.upsert_params, **self.additional_params}
        from pprint import pprint
        pprint(data)
        payload = json.dumps(data)

        resp = self.client.post(url=self.upsert_endpoint, data=payload, params=self.auth, headers=self.headers)
        assert resp.status_code == 200
