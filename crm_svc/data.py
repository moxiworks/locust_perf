from faker import Faker
mock = Faker()

upsert_endpoint = "/service/v1/contacts/upsert"

create_endpoint = "/service/v1/contacts"

auth = {
    "testing": "Staging"
}

create_params = {
        "agent_uuid": "60d6f848-38d7-4cdb-adf2-4aaea5e10283",
        "user_uuid": None,
        "given_name": None,
        "middle_name": None,
        "surname": None,
        "generation": "Sr",
        "company_name": "API TESTS",
        "job_title": None,
        "business_home_page": "https://georgesbiz.com",
        "body": "This is a good contact, I should make a note of it.",
        "gender": "f",
        "profession": "Veterinarian",
        "language": "en-US",
        "label_name": "Dr. George Orwell",
        "source": "zillow",
        "email_addresses": [
            {
              "priority": 1,
              "text": None
            }
        ],
        "im_addresses": [
            {
              "priority": 1,
              "text": "skype.handle.eg"
            }
        ],
        "phone_numbers": [
            {
              "key": "mobile",
              "text": "(360) 360-3600"
            }
        ],
        "contact_events": [
            {
              "key": "birthday",
              "text": "2021-10-07T18:17:38+00:00"
            }
        ],
        "relations": [
            {
              "key": "sister",
              "text": "Virginia Wolff"
            }
        ],
        "physical_addresses": [
            {
              "key": "home",
              "country_or_region": "US",
              "state": "Washington",
              "city": "Seattle",
              "postal_code": "98105",
              "neighborhood": "Wallingford",
              "street": "123 Seattle St.",
              "po_box": "401"
            }
          ],
        "social_media_profiles": [
            {
              "key": "facebook",
              "url": "https://www.facebook.com/example"
            }
        ],
        "contact_metadata": [
            {
              "name": "test",
              "value": "QA test"
            }
        ]
    }

upsert_params = {
        "agent_uuid": "60d6f848-38d7-4cdb-adf2-4aaea5e10283",
        "user_uuid": None,
        "on_multiple_match": "create",
        "search_attributes": {
            "given_name": "QA_first",
            "surname": "QA_last",
            "email_address": "QA@qatest.com",
        },
        "missing_fields_only": True,
        "given_name": "QA_first",
        "middle_name": mock.first_name(),
        "surname": "QA_last",
        "generation": "gen",
        "company_name": "company",
        "job_title": mock.state(),
        "business_home_page": "https://georgesbiz.com",
        "body": "This is a good contact, I should make a note of it.",
        "gender": "f",
        "profession": "Veterinarian",
        "language": "en-US",
        "label_name": "Dr. George Orwell",
        "source": "zillow",
        "email_addresses": [
            {
              "priority": 1,
              "text": "QA@qatest.com"
            }
          ],
        "im_addresses": [
            {
              "priority": 1,
              "text": "skype.handle.eg"
            }
          ],
        "phone_numbers": [
            {
              "key": "mobile",
              "text": "(360) 360-3600"
            }
          ],
        "contact_events": [
            {
              "key": "birthday",
              "text": "2021-10-07T18:17:38+00:00"
            }
          ],
        "relations": [
            {
              "key": "sister",
              "text": "Virginia Wolff"
            }
          ],
        "physical_addresses": [
            {
              "key": "home",
              "country_or_region": "US",
              "state": "Washington",
              "city": "Seattle",
              "postal_code": "98105",
              "neighborhood": "Wallingford",
              "street": "123 Seattle St.",
              "po_box": "401"
            }
          ]
        }

additional_params = {
    "social_media_profiles": [
        {
            "key": "facebook",
            "url": "https://www.facebook.com/example"
        }
    ],
    "contact_metadata": [
        {
            "name": "test",
            "value": "QA test"
        }
    ]
}

headers = {
        'Content-Type': 'application/json',
        'X-CLIENT-APP': 'web',
        'Accept': 'application/vnd.crm+json;version=1'
    }