from faker import Faker

mock = Faker()

v2_insec_comp_ag_endpoint = "/service/profile/v2_insecure/company/3139213/agents"

auth = {
    "testing": "ST"
}

insec_comp_ag_params = {
    "pgsize": 128,
}


headers = {
    'Content-Type': 'application/json',
    'X-CLIENT-APP': 'web',
    'Accept': 'application/vnd.crm+json;version=1'
}
