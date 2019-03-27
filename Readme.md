# Labbi

## Installation and setup

In order to be able to run Labbi on you local computer, you will need to follow the steps below.

1. Download the repository to a folder.
2. Download and install Python 3.7.
3. Download and install Django version 2.1.5+
4. Download and install MySQL 8 and configure a root user.
5. Download and install the following Python modules using pip:
  * django-tables2
  * django-filter
  * django-crispy-forms
  * django-composite-fields
  * django-registration
  * django-recaptcha
6. Open the terminal and log in to MySQL as a root user using the following command: 

   ```mysql -u root -p  ```
   
   Within MySQL, create a user and database.  Here are example commands for each<sup>[1](#myfootnote1)</sup>: 
   ```
   CREATE USER 'user'@'localhost' IDENTIFIED BY 'password';  
   GRANT ALL PRIVILEGES ON *.* TO 'user'@'localhost' WITH GRANT OPTION;
   ```
   Then exit MySQL.
7. 
6. Open the terminal and navigate to the folder where you downloaded the repository.  Go into the lims_project folder which contains the manage.py file.  Then run the following command: python3 manage.py runserver





<a name="myfootnote1">1</a>: If the code above does not work, try this one instead:
  ```
  create user user@localhost identified by 'password'
  GRANT ALL PRIVILEGES ON *.* TO user@localhost WITH GRANT OPTION;
  ```
