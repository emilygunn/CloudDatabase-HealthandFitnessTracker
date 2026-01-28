import firebase_admin
from firebase_admin import credentials, db

#Initialzing
cred = credentials.Certificate(".\important\itness-and-health-cse310-firebase-adminsdk-fbsvc-f6b92dbf08.json")
default_app = firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://console.firebase.google.com/u/0/project/fitness-and-health-cse310/firestore/databases/-default-/data'
})

#Ref
ref = db.reference("/info.json")

#Creating Health Info
    #Creates new entry of Date: Age, Weight, and Height
h_info_ref = ref.child('h_info')
h_info_ref.set({
    '1/27/26': {
        'Age': '19',
        'Weight': '120 lbs',
    }
})