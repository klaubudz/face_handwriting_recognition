import requests
import json

URL = 'http://127.0.0.1:8080/api'


def get_request(path):
    req = requests.get(URL + path)
    return req.content.decode('utf8').replace("'", '"')


def post_request(path,data):
    req = requests.post(URL + path, data=data)
    return req.content.decode('utf8').replace("'", '"')


def get_groups_list():
    response = get_request('/groups/')
    groups = json.loads(response)
    return groups

def get_group_members(group_id):
    response = get_request('/groups/members/{}/'.format(group_id))
    return json.loads(response)

def get_people_list():
    response = get_request('/people/')
    people = json.loads(response)
    return people

def get_person(person_id):
    response = get_request('/people/get/' + str(person_id))
    return json.loads(response)


def add_attendance(date, group_id):
    response = post_request('/attendances/', data={'date': date, 'group': group_id})
    return json.loads(response)


def add_attendance_member(attendance_id, member_id):
    requests.post(URL + '/attendances/addmember/', data={'attendance_id': attendance_id, 'member_id': member_id})

def get_subjects_list():
    response = get_request('/subjects/')
    subjects = json.loads(response)
    return subjects

def add_grade(subject_id, description, date, person_id, grade):
    requests.post(URL + '/grades/', data={'subject': subject_id, 'description': description, 'date': date, 'person': person_id, 'number': grade })
