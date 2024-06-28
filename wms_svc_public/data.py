from faker import Faker
import base64

def auth_headers():

    platform_id = "b9405ada-d8b8-11e8-890b-52540015d263"
    platform_secret = "Zrj5Ja7lmfd2LKotLlk9OAtt"
    credentials = F"{platform_id}:{platform_secret}"
    encoded_credential_bytes = base64.b64encode(credentials.encode("utf-8"))
    access_token = str(encoded_credential_bytes, "utf-8")
    headers = {
        'Authorization': F'Basic {access_token}',
        'Accept': 'application/vnd.moxi-platform+json;version=1',
        'Content-Type': 'application/json'
    }
    return headers


mock = Faker()

#Params
groups_params = {
    "agent_uuid": "cd3f6fdc-046c-4196-b9c0-796901a6544f",
    "page_number": 5,
}


#Endpoints
groups_endpoint = f"/api/groups/e2E4NTRkYTQwLWViNGUtNDQ4Zi1hNzQ1LWMyOTZlY2U2ODMxNn0=__MWID__"
groups_search_endpoint = f"/api/groups"
#Headers
headers = auth_headers()

