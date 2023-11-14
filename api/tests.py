from django.test import TestCase

import requests

data = {
    "full_name":"Jamshid",
    "phone_number":"+998999119111",
    "amount":"23000",
    "type": "legal"
}



response = requests.post(
    url = "http://127.0.0.1:8000/api/v1/sponsor-create/"
    data = data
    )
