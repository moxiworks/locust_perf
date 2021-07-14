import requests
from locust import HttpUser, task, between
from locust_plugins.csvreader import CSVReader

# agent_uuids = CSVReader("agent_uuids.csv")
# office_ids = CSVReader("office_ids.csv")
# company_ids = CSVReader("company_ids.csv")


class PerfBranding(HttpUser):
    wait_time = between(0.5, 1)

    """
    Flush branding cache once before running the tests
    """
    try:
        print("START flushing branding cache...")
        resp = requests.get("https://svc-qa.moxiworks.com/service/v1/branding/flush_branding")
        resp.raise_for_status()
        print("DONE flushing branding cache.\n")
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)

    def __init__(self, parent):
        super(PerfBranding, self).__init__(parent)
        self.ag_uuid = "6e02aeec-991f-4903-93ae-280b44c8bbb6"
        self.comp_id = "3139213"
        self.office_id = "21684435"

    @task(15)
    def get_agent(self):
        self.client.get(url=F"/service/v1/branding/agent/{self.ag_uuid}?locale=en-US", name="Agent")

    @task(4)
    def get_branding(self):
        self.client.get(url=F"/service/v1/branding/company/{self.comp_id}?locale=en-US", name="Company")

    @task(1)
    def get_office(self):
        self.client.get(url=F"/service/v1/branding/office/{self.office_id}?locale=en-US", name="Office")
