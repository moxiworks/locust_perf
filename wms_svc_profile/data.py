from faker import Faker

mock = Faker()

#Params
v2_insec_comp_ag_uuid = 3139213
v2_insec_office_ag_uuid = 14236533
windermere_uuid = 1234567
publickey = "1syzu"

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

syndication_prof_params = {
    "company_uuid": windermere_uuid,
    "pgsize": 50
}

syndication_prof_uuid = "c0384a13-504a-4613-bb8a-743dbd871bb5"
web_user_uuid = "e14120d3-19d4-4724-968f-7b5d9eaba7a6"

attr_search_params = {
    "user_attr_key": "company_designation",
    "user_attr_value": "Sales Representative"
}
search_association_params = {
    "web_user_uuid": web_user_uuid
}

#Endpoints
v2_insec_comp_ag_endpoint = f"/service/profile/v2_insecure/company/{v2_insec_comp_ag_uuid}/agents"
v2_insec_office_ag_endpoint = f"/service/profile/v2_insecure/office/{v2_insec_office_ag_uuid}/agents"
v2_comp_ag_endpoint = f"/service/profile/v2_insecure/company/{v2_insec_comp_ag_uuid}/agents"
v2_office_ag_endpoint = f"/service/profile/v2_insecure/office/{v2_insec_office_ag_uuid}/agents"
public_key_endpoint = f"/service/profile/v2/public_key/{publickey}"
v2_endpoint = "/service/v1/profile/"
syndication_profile_endpoint = "/service/profile/v2/syndication/profile"
v2_profile_endpoint = "service/profile/v2/"
v2_profile_attr_search_endpoint = "/service/profile/v2/attribute"
v2_profile_search_association_endpoint = "/service/profile/v2/search_by_association"
v2_for_sso_endpoint = "service/profile/v2/for_sso/"


#Headers
headers = {
    'Content-Type': 'application/json',
    'X-CLIENT-APP': 'web',
    'Accept': 'application/vnd.crm+json;version=1'
}