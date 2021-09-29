This is example website for studying Flask

Three menus in navbar (templates\components\layout.html)
- Home (index.html) - /
- Study (lecture\lecture_templates\lecture.html) - /lecture
- Meetups (meetup\meetup_templates\meetup.html) - /meetup
lecture and meetup are registered as blueprint in __init__.py

- Signup (signup.html) - /signup (When you click "Sign-up" button from Home) 
    : Store first name, last name, email, password information in the user database
- Add new lecture(addlecture.html) - /addlecture (When you click "Add new lecture" button from Study)
    : Store subject, start date, end date, description, price in the lesson database

Images: static\images
CSS: static\css\main.css

