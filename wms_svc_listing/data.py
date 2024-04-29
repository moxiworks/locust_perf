from faker import Faker

mock = Faker()

dedupe_endpoint = "/service/v1/listing/search/a16c386c-f1b0-41db-b22b-7f9dc1917a0f/nn/dedupe"

auth = {
    "testing": "ST"
}

dedupe_params = {
    "cdom_min": 80,
    "dedupe": 1,
    "pgsize": 500,
    "include_agent_data": True,
    "currency": "USD",
    "site_type": "Agent Website",
}

headers = {
    'Content-Type': 'application/json',
    'X-CLIENT-APP': 'web',
    'Accept': 'application/vnd.crm+json;version=1'
}
