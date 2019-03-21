Wymagania: 
	- Python3
	- PostgreSQL
	- pip3 ( sudo apt install python3-pip )
	
Pakiety:
	- face_recognition
	- django
	- requests
	- json
	- base64
	- djangorestframework
	- markdown
	- django-filter
	- openCV (instalacja: https://docs.opencv.org/master/d7/d9f/tutorial_linux_install.html )

Instalacja pakietów: pip3 install nazwa_pakietu

==== Aplikacja webowa ====

Polecenie uruchomienia: python3 manage.py runserver 8081

Strona web: http://localhost:8081/faceRecognitionWebsite

Panel administracyjny: http://127.0.0.1:8081/admin/faceRecognitionWebsite/

Obsługa panelu administracyjnego: 
	-> Login: admin
	-> Hasło: adminadmin

W pliku /FaceRecogniser/mysite/settings.py należy podać informacje dotyczące używanej bazy danych, np.:
	DATABASES = {
	    'default': {
	        'ENGINE': 'django.db.backends.postgresql_psycopg2',
	        'NAME': 'facedb',
	        'USER': 'admin',
	        'PASSWORD': 'admin',
	        'HOST': 'localhost',
	        'PORT': '',
	    }
	}

-------------------------------------------------------------------------------------------------------

Aplikacje konsolowe wymagają dostępu do kamery.

==== Aplikacja konsolowa - lista obecności ====

Polecenie uruchomienia: python3 app.py
Zakończenie działania: przycisk 'esc'.


==== Aplikacja konsolowa - oceny ====

Polecenie uruchomienia: python3 app_hwrt.py
Zakończenie działania: przycisk 'q'.

UWAGA !!! 
Do działania aplikacji wymagane jest podanie Google API Key. Należy go wkleić w pliku /face-recognition-client/terminal_hwrt.py w metodzie: 

def send_request(self,content):
    URL = 'https://vision.googleapis.com/v1/images:annotate?key=moj_google_api_key

