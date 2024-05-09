from faker import Faker

mock = Faker()
v2_insec_comp_ag_uuid = 3139213
v2_insec_comp_ag_endpoint = f"/service/profile/v2_insecure/company/{v2_insec_comp_ag_uuid}/agents"
v2_endpoint = "/service/v1/profile/"

alt_off_ag_uuids = [
    "9d692c32-4182-4431-8ffc-ae02ef5bd19c",
    "bd8ea968-4737-4d21-b937-18f6851f5a3d",
    "373093d2-19fa-4b97-a451-2f2871875377",
    "a5b7a699-ea7c-4429-8f8e-e6b00ce02a1f",
    "740e315a-8957-464c-be2f-3cd2b15d69ea",
    "7654c231-578d-4ca5-96be-8e28cc0be27c"
]

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
