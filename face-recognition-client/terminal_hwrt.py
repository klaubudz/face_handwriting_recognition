import face_service_client
import face_recognition
import cv2
from _datetime import datetime
import keyboard
import base64
import requests
import json


class Terminal_HWRT:

    def __init__(self):
        self.selected_subject_id = 0
        self.subjects = face_service_client.get_subjects_list()
        self.groups = []
        self.people = face_service_client.get_people_list()
        self.description = ""
        self.recognised = ""
        self.person_data = []
        self.found_person = None

    def print_subjects(self):
        if self.subjects is None:
            print("There are no subjects!")
        else:
            print('Subjects: ')
            print('---------')
            for subject in self.subjects:
                print(subject['name'], ', id:', subject['id'])
            print('-------------------------------------------')

    def check_if_subject_exists(self, subject_id):
        for subject in self.subjects:
            if subject['id'] == subject_id:
                return True
        return False

    def read_subject(self):
        while True:
            try:
                number = int(input('Please type subject id to start scanning:' + '\n'))
                if self.check_if_subject_exists(number):
                    self.selected_subject_id = number
                    print('-------------------------------------------')
                    return
            except ValueError:
                print("Not a number")

    def read_description(self):
        desc = input("Please type grade description:" + '\n')
        self.description = desc
        print('-------------------------------------------')

    def print_instructions(self):
        print("=====================================================")
        print("Place text in front of the camera after the window opens")
        print("Press space to save the picture")
        print("Press esc to finish")
        print("=====================================================")

    def send_request(self,content):
        URL = 'https://vision.googleapis.com/v1/images:annotate?key='

        content = {'content': content}
        features = [{'type': 'DOCUMENT_TEXT_DETECTION'}]
        img_context = {'languageHints': ['pl']}
        data = {'requests': [{'image': content, 'features': features, 'imageContext': img_context}]}
        req = requests.post(URL, data = json.dumps(data))
        return req.text

    def split_recognised_data(self):
        self.person_data = self.recognised.split()
        print(self.person_data)
        return(self.person_data)

    def find_person_by_names(self):
        name = self.person_data[0]
        surname = self.person_data[1]
        grade = float(self.person_data[2])
        for person in self.people:
            if person["name"].upper() == name.upper() and person["surname"].upper() == surname.upper():
                self.found_person = person
                face_service_client.add_grade(self.selected_subject_id, self.description, datetime.now(), person['id'], grade)
                print('Added')
                print('')
                return
        print("Person not found")
        return None

    def scan_hwrt(self):
        video_capture = cv2.VideoCapture(0)

        print("Please press space to scan grade or esc to end program")
        while True:
            ret, frame = video_capture.read()
            cv2.imshow('Video', frame)

            key = cv2.waitKey(1)
            # space == 32 - hit space to continue reading
            if key == 32:
                retval, buffer = cv2.imencode('.jpg', frame)

                encoded_string = base64.b64encode(buffer).decode("utf-8")
                response_text = self.send_request(encoded_string)
                response = json.loads(response_text)
                self.recognised = response["responses"][0]["textAnnotations"][0]["description"]
                #print(self.recognised)
                self.split_recognised_data()
                self.find_person_by_names()
            elif key == 27:
                video_capture.release()
                break
