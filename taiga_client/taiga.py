import re
import unicodedata
from json import dumps
from json.decoder import JSONDecodeError

import requests

from taiga_client.models.project import Project
from taiga_client.models.project_item import ProjectItem


class Taiga:
    headers = {'Content-Type': 'application/json'}

    def _request(self, req, endpoint, data=None):
        r = req(
            f'{self.api_url}/{endpoint}',
            headers=self.headers, data=dumps(data))
        # if r.status_code != 200:
        #     raise Exception(f'{r.url}\n{r.text}')
        try:
            r = r.json()
            if '_error_message' in r:
                return None
            return r
        except JSONDecodeError:
            return r.text

    def get(self, endpoint):
        return self._request(requests.get, endpoint)

    def delete(self, endpoint):
        return self._request(requests.delete, endpoint)

    def post(self, endpoint, data):
        return self._request(requests.post, endpoint, data)

    def __init__(self, host, normal_auth):
        self.api_url = f'{host}/api/v1'
        username, password = normal_auth
        self.username = username
        auth_data = {
            'type': 'normal',
            'username': username,
            'password': password
        }
        r = self.post('auth', auth_data)
        self.headers['Authorization'] = f'Bearer ' + r['auth_token']

    def get_project_slug(self, name):
        # https://github.com/django/django/blob/70d95682b1be6a85abdeaea0205a897f7530f8bc/django/utils/text.py#L394  # noqa: E501
        name = f'{self.username} {name}'
        name = unicodedata.normalize(
            'NFKD', name).encode('ascii', 'ignore').decode('ascii')
        name = re.sub(r'[^\w\s-]', '', name).strip().lower()
        return re.sub(r'[-\s]+', '-', name)

    def projects(self):
        r = self.get('projects')
        if r is None:
            return None
        r = [ProjectItem(**project_item) for project_item in r]
        return r

    def project(self, id):
        r = self.get(f'projects/{id}')
        if r is None:
            return None
        return Project(**r)

    def project_by_slug(self, slug):
        r = self.get(f'projects/by_slug?slug={slug}')
        if r is None:
            return None
        return Project(**r)

    def create_project(
        self, name, description, creation_template=1, is_private=True,
            is_backlog_activated=True, is_issues_activated=True,
            is_wiki_activated=True, **kwargs):
        data = dict(
            name=name, description=description,
            creation_template=creation_template, is_private=is_private,
            is_backlog_activated=is_backlog_activated,
            is_issues_activated=is_issues_activated,
            is_wiki_activated=is_wiki_activated,
            **kwargs)
        r = self.post('projects', data)
        if r is None:
            return None
        return Project(**r)

    def delete_project(self, id):
        r = self.delete(f'projects/{id}')
        return r


"""
class Taiga:

    status_ids = {}
    status_map = {}
    headers = {'Content-Type': 'application/json'}
    def build_statuses(self):
        url = f'{self.api_url}/projects/by_slug?slug={self.project_slug}'
        r = self._request(requests.get, url)
        for taiga_status in r.us_statuses:
            self.status_ids[taiga_status.name] = taiga_status.id
        for jira, taiga in self.statuses:
            self.status_map[jira] = self.status_ids[taiga]
        self.project_id = r.us_statuses[0].project_id

    def __init__(self, config):
        super(Taiga, self).__init__()
        for key in config.keys():
            setattr(self, key, config[key])
        self.build_statuses()

    def _data_for_userstories(self, row):
        row = bunchify(row)
        closed = False
        blocked = False
        tags = row.Labels.split(', ')
        status = self.status_map[row.Status]
        subject = f'{row.Key}: {row.Summary}'
        description = (
            f'''Description: {row.Description}
            Reporter: {row.Reporter}
            Assignee: {row.Assignee}
            Watchers: {row.Watchers}
            Sub-Tasks: {row['Sub-Tasks']}
            Linked Stories: {row['Linked Issues']}''')
        if row.Status in self.closed_statuses:
            closed = True
        if row.Status in self.blocked_statuses:
            blocked = True
        postdict = {
            "assigned_to": None,
            "backlog_order": 2,
            "blocked_note": "",
            "client_requirement": False,
            "description": description,
            "is_blocked": blocked,
            "is_closed": closed,
            "kanban_order": 37,
            "milestone": None,
            "points": {},
            "project": self.project_id,
            "sprint_order": 2,
            "status": status,
            "subject": subject,
            "tags": tags,
            "team_requirement": False,
            "watchers": [],
        }
        return json.dumps(postdict)

    def create_userstories(self):
        url = f'{self.api_url}/userstories'
        print('Posting stories to Taiga (this could take a while)', flush=True)
        with open(self.csv_dump) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data = self._data_for_userstories(row)
                r = requests.post(url, headers=self.headers, data=data)
                print(r.json(), end="", flush=True)
"""
