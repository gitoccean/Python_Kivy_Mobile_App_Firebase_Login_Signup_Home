# its Just for configuration with firebasse, either it is running to store data in firebase through shell or extract during feedup.



import pyrebase

firebaseConfig = {
  'apiKey': "AIzaSyD9N2IBF0NS-9FZMbFIW_ON1Tq94rkXZOY",
  'authDomain': "pythonauthproject-c3fc8.firebaseapp.com",
  'databaseURL': "https://pythonauthproject-c3fc8-default-rtdb.firebaseio.com/",
  'projectId': "pythonauthproject-c3fc8",
  'storageBucket': "pythonauthproject-c3fc8.appspot.com",
  'messagingSenderId': "679814430731",
  'appId': "1:679814430731:web:9790480fa660f4cc41870e"
}

firebase = pyrebase.initialize_app(firebaseConfig)
mAuth = firebase.auth()

email = input("Enter Email:  ")
password = input("Enter Password:  ")

try:
    mAuth.create_user_with_email_and_password(email=email,password=password)
    print('User created.')
except:
    print("Email already exist.")

try:
    mAuth.sign_in_with_email_and_password(email=email,password=password)
    print('User logged in.')
except:
    print("Invalid Credentials.")
