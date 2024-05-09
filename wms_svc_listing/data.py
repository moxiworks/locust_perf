from faker import Faker

mock = Faker()
dedupe_ag_uuid = "a16c386c-f1b0-41db-b22b-7f9dc1917a0f"
search_dedupe_ag_uuid = "6e02aeec-991f-4903-93ae-280b44c8bbb6"
dedupe_endpoint = f"/service/v1/listing/search/{dedupe_ag_uuid}/nn/dedupe"
search_dedupe_endpoint = f"/service/v1/listing/search/{search_dedupe_ag_uuid}/company"
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

search_dedupe_params = {
    "dedupe": 1,
    "pgsize": 100,
    "include_agent_data": True,
    "currency": "USD",
    "site_type": "Agent Website",
    "from_app": "aws:https://ahearl.st.withwre.com"
}

headers = {
    'Content-Type': 'application/json',
    'X-CLIENT-APP': 'web',
    'Accept': 'application/vnd.crm+json;version=1'
}
