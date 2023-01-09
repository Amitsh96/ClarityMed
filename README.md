# ClarityMed
Project &lt;Group #35>


installation:

1. at first need to install  the file: requirements.txt by typing in the terminal :  ' pip install -r requirements.txt ' if you open the right path in the computer.
2. for the static files (images,css etc..) in the project you need the path in settings.py for example:" 'D:/GitHub/ClarityMed/claritymedapp/static', ".
3. external software: xampp for the database. (can be downloaded from the internet)
4. start server from xampp.
5. in visual code, type in the terminal: ' python manage.py makemigrations ' right after that command , run this line :  ' python manage.py migrate ' this will ensure that youl have the database.
6. run 'python manage.py createsuperuser' and create an admin user so you can access the site.
7. run ' python manage.py runserver ' to run the server.
8. access : http://127.0.0.1:8000/admin/ and in useres section add your superuser to the admin group so you can access all urls.
9. pay attention that the database is empty from all of the products and users we created LOCAL on our computer.
10. to enjoy the whole site you can create few users from the register site, they will be added automaticlly to the clients group and you can create in  http://127.0.0.1:8000/admin/ the rest of the doctor and receptionist and also all the equipments.
11. now you can access http://127.0.0.1:8000/claritymedapp/index.

ENJOY! 
