import requests
import pandas as pd
from locust import HttpUser, task, between

csv_files = ['agent', 'company', 'office']
path = 'branding/csv'

dataframes_list = []

for i in range(len(csv_files)):
    temp_df = pd.read_csv(f"{path}/{csv_files[i]}.csv")
    dataframes_list.append(temp_df)


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
        self.agents = dataframes_list[0]
        self.companies = dataframes_list[1]
        self.offices = dataframes_list[2]

    @task(15)
    def get_agent(self):
        for _, ag in self.agents.iterrows():
            a = self.client.get(url=F"/service/v1/branding/agent/{ag[0]}?locale=en-US", name="Agents")
            a.raise_for_status()

    @task(4)
    def get_companies(self):
        for _, br in self.companies.iterrows():
            a = self.client.get(url=F"/service/v1/branding/company/{br[0]}?locale=en-US", name="Companies")
            a.raise_for_status()

    @task(1)
    def get_office(self):
        for _, off in self.offices.iterrows():
            a = self.client.get(url=F"/service/v1/branding/office/{off[0]}?locale=en-US", name="Offices")
            a.raise_for_status()
