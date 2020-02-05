import requests


class AtsManagementClient:
    def __init__(self, tenant, url):
        self.tenant = tenant
        self.url = url
        self.ats_url = f"{url}/{tenant}/ats"

    def get_ats_config(self):
        response = requests.get(self.ats_url)
        return response

    def post_ats_config(self, payload):
        response = requests.post(self.ats_url, json=payload)
        return response
