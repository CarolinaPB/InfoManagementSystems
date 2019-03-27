# Labbi

## Installation and setup

In order to be able to run Labbi on you local computer, you will need to follow the steps below.

1. Download the repository to a folder.
2. Download and install Python 3.7.
3. Download and install Django version 2.1.5+
4. Download and install MySQL 8 and configure a root user.
5. Download and install the following Python modules, for example using pip:
  * [django-tables2](https://django-tables2.readthedocs.io/en/latest/)
  * [django-filter](https://django-filter.readthedocs.io/en/master/)
  * [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/)
  * [django-composite-fields](https://pypi.org/project/django-composite-field/)
  * [django-registration](https://django-registration.readthedocs.io/en/3.0/)
  * [django-recaptcha](https://github.com/praekelt/django-recaptcha)
6. Open the terminal and log in to MySQL as a root user using the following command: 

   ```mysql -u root -p  ```
   
   Within MySQL, create a user and database.  Here are example commands for each<sup>[1](#myfootnote1)</sup>: 
   ```
   CREATE USER 'USER'@'localhost' IDENTIFIED BY 'PASSWORD';  
   GRANT ALL PRIVILEGES ON *.* TO 'USER'@'localhost' WITH GRANT OPTION;
   ```
   Then exit MySQL.
7. Open the terminal and navigate to the folder where you downloaded the repository.  Go into the lims_project folder which contains the manage.py file.  From here, run the following commands:
   ```
   python3 manage.py makemigrations
   python3 manage.py migrate
   python3 manage.py createsuperuser
   ```
   The first two commands will migrate the database structure defined in the Django code to the MySQL server.  The third command will create an admin account for the Labbi.
8. Create a file called database_config.py in the InfoManagementSystems/lims_project/labbyims folder and include the following code:
   ```
   database_name="YOUR_DB_NAME"
   database_user="USER"
   database_password="PASSWORD"
   
   email = "YOUR_EMAIL
   email_password="YOUR_PASSWORD"
   ```
6. Finally, in order to start the server, run the followin command in the same directory: 
   ```
   python3 manage.py runserver
   ```


<a name="myfootnote1">[1]</a>: If the code above does not work, try this one instead:
  ```
  create user USER@localhost identified by 'PASSWORD';
  GRANT ALL PRIVILEGES ON *.* TO USER@localhost WITH GRANT OPTION;
  ```
