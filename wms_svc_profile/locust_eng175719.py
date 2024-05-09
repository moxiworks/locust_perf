from faker import Faker
from locust import HttpUser, task
from data import (v2_insec_comp_ag_endpoint, v2_insec_office_ag_endpoint, v2_comp_ag_endpoint, v2_office_ag_endpoint,
                  public_key_endpoint, syndication_profile_endpoint, v2_profile_endpoint,
                  v2_profile_attr_search_endpoint, v2_for_sso_endpoint, v2_profile_search_association_endpoint,
                  insec_comp_ag_params, syndication_prof_params, attr_search_params, search_association_params,
                  syndication_prof_uuid, auth, headers)


class PerfProfileSvc(HttpUser):
    def __init__(self, parent):
        super(PerfProfileSvc, self).__init__(parent)
        self.v2_insec_comp_ag_endpoint = v2_insec_comp_ag_endpoint
        self.insec_comp_ag_params = insec_comp_ag_params
        self.v2_insec_office_ag_endpoint = v2_insec_office_ag_endpoint
        self.v2_comp_ag_endpoint = v2_comp_ag_endpoint
        self.v2_office_ag_endpoint = v2_office_ag_endpoint
        self.public_key_endpoint = public_key_endpoint
        self.syndication_profile_endpoint = syndication_profile_endpoint
        self.v2_profile_endpoint = v2_profile_endpoint
        self.v2_profile_attr_search_endpoint = v2_profile_attr_search_endpoint
        self.v2_for_sso_endpoint = v2_for_sso_endpoint
        self.v2_profile_search_association_endpoint = v2_profile_search_association_endpoint
        self.syndication_prof_params = syndication_prof_params
        self.attr_search_params = attr_search_params
        self.search_association_params = search_association_params
        self.profile_uuid = syndication_prof_uuid
        self.auth = auth
        self.headers = headers
        self.mock = Faker()

    @task()
    def get_v2_insec_comp_ag(self):
        try:
            resp = self.client.get(url=self.v2_insec_comp_ag_endpoint,
                                   params=self.insec_comp_ag_params)
            assert resp.status_code == 200
        except Exception as e:
            print("request_failed", e)

    @task()
    def get_v2_insec_office_ag(self):
        try:
            resp = self.client.get(url=self.v2_insec_office_ag_endpoint,
                                   params=self.insec_comp_ag_params)
            assert resp.status_code == 200
        except Exception as e:
            print("request_failed", e)

    @task()
    def get_v2_comp_ag(self):
        try:
            resp = self.client.get(url=self.v2_comp_ag_endpoint,
                                   params={**self.insec_comp_ag_params, **self.auth})
            assert resp.status_code == 200
        except Exception as e:
            print("request_failed", e)

    @task()
    def get_v2_office_ag(self):
        try:
            resp = self.client.get(url=self.v2_office_ag_endpoint,
                                   params={**self.insec_comp_ag_params, **self.auth})
            assert resp.status_code == 200
        except Exception as e:
            print("request_failed", e)

    @task()
    def get_public_key(self):
        try:
            resp = self.client.get(url=self.public_key_endpoint,
                                   params=self.auth)
            assert resp.status_code == 200
        except Exception as e:
            print("request_failed", e)

    @task()
    def get_profile_v2(self):
        try:
            resp = self.client.get(url=f"{self.v2_profile_endpoint}{self.profile_uuid}",
                                   params=self.auth)
            assert resp.status_code == 200
        except Exception as e:
            print("request_failed", e)

    @task()
    def get_profile_v2_syndication(self):
        try:
            resp = self.client.get(url=f"{self.syndication_profile_endpoint}{self.profile_uuid}",
                                   params=self.auth)
            assert resp.status_code == 200
        except Exception as e:
            print("request_failed", e)

    @task()
    def get_profile_v2_syndication_search(self):
        try:
            resp = self.client.get(url=self.syndication_profile_endpoint,
                                   params={**self.syndication_prof_params, **self.auth})
            assert resp.status_code == 200
        except Exception as e:
            print("request_failed", e)

    # @task()
    # def get_profile_v2_attr_search(self):
    #     try:
    #         resp = self.client.get(url=self.v2_profile_attr_search_endpoint,
    #                                params={**self.attr_search_params, **self.auth})
    #         assert resp.status_code == 200
    #     except Exception as e:
    #         print("request_failed", e)

    @task()
    def get_profile_v2_for_sso(self):
        try:
            resp = self.client.post(url=f"{self.v2_for_sso_endpoint}{self.profile_uuid}",
                                    params={**self.attr_search_params, **self.auth})
            assert resp.status_code == 200
        except Exception as e:
            print("request_failed", e)

    @task()
    def get_profile_v2_search_assoc(self):
        try:
            resp = self.client.get(url=self.v2_profile_search_association_endpoint,
                                    params={**self.search_association_params, **self.auth})
            assert resp.status_code == 200
        except Exception as e:
            print("request_failed", e)
