
# ClarityMed <Group #35>

ClarityMed is a hospital services website designed to provide a smooth and convenient experience for patients, doctors and receptionists. The site offers a variety of features to make it easier for patients to access the medical care they need, including scheduling appointments, treatment status, etc.

Overall, ClarityMed aims to provide a comprehensive healthcare management solution, providing access to valuable medical information and resources to all parties involved, which will improve the overall healthcare experience for patients, while helping healthcare providers better manage their patients and services. .


## Run Locally

Clone the project.

```bash
  git clone https://github.com/Amitsh96/ClarityMed
```

Go to the project directory.

```bash
  cd ClarityMed/claritymedapp
```

Install requirements.txt.

```bash
  pip install -r requirements.txt
```

In settings.py  STATICFILES_DIRS add: 

```bash
  YOUR - PATH /static for ex. " 'D:/GitHub/ClarityMed/claritymedapp/static', "
```

Install XAMPP and start the servers.

```bash
  https://www.apachefriends.org/
```

Make migrations and migrate.
This will ensure that youl have the database.

```bash
  1. python manage.py makemigrations
  2. python manage.py migrate
```




Create an admin user so you can access the site.
```bash
  python manage.py createsuperuser
```

Start the server

```bash
  python manage.py runserver
```

Add your superuser to the admin group so you can access all urls.
```bash
  http://127.0.0.1:8000/admin/ 
```

Pay attention that the database is empty from all of the products and users we created LOCAL on our computer.

To enjoy the whole site you can create few users from the register site, they will be added automaticlly to the clients group and you can create in the adnmin site the rest of the doctor and receptionist and also all the equipments.
now you can access:
```bash
  http://127.0.0.1:8000/claritymedapp/index
```

Enjoy the website!
 
## Running Tests

To run tests, run the following command

```bash
  python mangae.py test
```


## Authors

- [@tomernetzer14](https://github.com/tomernetzer14)
- [@Amitsh96](https://github.com/Amitsh96)
- [@rozales](https://github.com/rozales)

