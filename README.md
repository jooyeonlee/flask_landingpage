This is example website for studying Flask

Three menus in navbar (templates\components\layout.html)
- Home (index.html) - /
- Signin (signin.html) - /signin
- Study (lecture\lecture_templates\lecture.html) - /lecture
- Meetups (meetup\meetup_templates\meetup.html) - /meetup
lecture, meetup, and user are registered as blueprint in __init__.py

- Signup (signup.html) - /signup (When you click "Sign-up" button from Home) 
    : Store first name, last name, email, password information in the user database
- Add new lecture(addlecture.html) - /addlecture (When you click "Add new lecture" button from Study)
    : Store subject, start date, end date, description, price in the lesson database

- When user log-in, he/she can see the Add New Lecture button in lecture page and <Username> menu in navbar
- Profile: See user data (/profile)
- Edit User Profile: Edit first name, last name, password (/editprofile)
- Sign out: log out from web page (/logout)

Images: static\images
CSS: static\css\main.css

