![alt text](https://github.com/geoeskel/dog-bone/blob/master/media/wireframes/top%20image.jpg)

# Dog & Bone

[Deployed website is found here](https://dog-bone.herokuapp.com/)

This project aims to create a functional e-commerce website providing dog food, toys, accessories and clothes.
There is an informational bit about dog feeding and, in the future, detailed information about all of the dog breeds and how to properly feed them

The primary target group is: dog owners


# Design 
I wanted the store to have a cozy and comfortable theme based on Autumn colours. It has a delicate contrasts and toned colors and should resemble the client an autumn park with beautiful golden-brown colours. I used the below tool to create the website theme:
https://coolors.co/

1.	Colour Scheme
- The 4 colors used are: Alloy Orange, Almond, Seal Brown, Russian Violet
![Color Palette](https://github.com/geoeskel/dog-bone/blob/master/media/wireframes/coolors.JPG)

2.	Typography
- I used Blinker font family for this project, it is the main font used throughout the store. It is a simple-looking font that works well with the website’s design; it is both attractive and appropriate
![Nanum Gothic](https://github.com/geoeskel/dog-bone/blob/master/media/wireframes/font.JPG)

3.	Imagery
- The background image works well with the rest of the design and allow for good color contrast. It gives the website a calm, aesthetic look.

4. 	Icons
- I used Font Awesome 6 for their variety and flexibility of their icons


# UX
This database is designed for anyone who would like to purchase dog items, whether those would be food, clothes, toys or other accessories.
It also aims to inform the client about how to feed their dog.

## User stories
1.	Client goals
- As a client, I want to be able to view a list of products, so that I can select some of them to purchase
- As a client, I want to be able to view each product details, so that I can check the price, description, rating, image and sizes
- As a client, I want to be able to view a total of all my purchases at any time so that I can check how much money I am spending
- As a client, I want to be able to sort through the list of products, so that I can identify the best rated, priced and product categories
- As a client, I want to be able to sort a specific product category, so that I can find the best priced or rated in each specific category and/or sort the category by name
- As a client, I want to be able to sort multiple categories at the same time, so that I can find the best rated or priced item across a broader category (e.g. Dog Food)
- As a client, I want to be able to search for a product by name and/or description, so that I can find a specific product I want to purchase
- As a client, I want to be able to select the size and amount of the product I am buying, so that I can make sure I don't accidentally select a wrong product or size
- As a client, I want to be able to easily select the size and quantity of a product when purchasing it, so that I can make sure I don't accidentally select the wrong product, size of amount
- As a client, I want to be able to view items in my basket to be purchased, so that I can check the total cost of my items and make sure which Items I will receive
- As a client, I want to be able to adjust and amount of individual items in my basket, so that I can easily make changes before the checkout
- As a client, I want to be able to easily enter my payment information, so that I can check out without any problems
- As a client, I want to be able to make sure my personal payment information ios safe and secure, so that I can confidently provide the needed information for the purchase
- As a client, I want to be able to view an order confirmation after the checkout, so that I can verify I haven't made any mistakes
- As a client, I want to be able to receive a confirmation e-mail after checking out, so that I can keep the confirmation of what I have purchased 

2.	Shop user goals
- As a shop user, I want to be able to easily register for an account so that I can have a personal account and be able to check my profile
- As a shop user, I want to be able to easily log in and out, so that I can access my personal information
- As a shop user, I want to be able to reset my password, so that I can recover access to my account
- As a shop user, I want to be able to have a personalized user profile, so that I can check my personal order history, order information and delivery details

3.	Shop owner goals
- As a shop owner, I want to be able to add a product, so that I can add new items to my shop
- As a shop owner, I want to be able to edit and update the product, so that I can change product prices, amounts, images and other criteria
- As a shop owner, I want to be able to delete a product, so that I can remove items that are no longer for sale
- As a shop owner, I want to be able to make sure only I can add/edit/delete items from my shop, so that I can be confident in the security of the website and know that noone else can make changes to my items database

 
# Wireframes

1.	Plan #1: https://github.com/geoeskel/dog-bone/blob/master/media/wireframes/1.jpg
2.	Plan #2: https://github.com/geoeskel/dog-bone/blob/master/media/wireframes/2.jpg
3.	Plan #3: https://github.com/geoeskel/dog-bone/blob/master/media/wireframes/3.jpg
3.	Plan #4: https://github.com/geoeskel/dog-bone/blob/master/media/wireframes/4.jpg
4.	End-effect: https://github.com/geoeskel/dog-bone/blob/master/media/wireframes/top%20image.jpg


# Features

## Navbar 
1.	Responsive navbar with a book icon ‘hamburger’ on devices with a screen width smaller than 992px 
2.	Each link will take the user to the designated pages
3. 	There is a link to the home page in the top page logo (dog & bone) and with the icon ‘hamburger’ on devices with a screen width smaller than 992px 
4.	There are links for the all products, dog food, dog equipment, dog wear, my account (with login and register links) and a shopping basket
5.	When the user logs in, the additional links appear: profile, log out
6.	When the admin/superuser logs in, an additional link appears inside the my account: manage products

## Home
1.	There is a welcome message on the left part of the page
2.	User can search the shop using the search bar on top of the page
3.	Under the welcome message is the shop here button taking the users to the all products page
4.  Under the navbar categories is a link to the dog feeding information page that user can click

## Register’
1.	A form to fill in to register an account
2.	There is a link to the login page in case the user already has an account
3. 	If the user inputs an incorrect information to the form, a message will give the user feedback
3.	Once registered, a pop-up attention box will give user feedback
4.	Once registered, user will be asked to verify their email address; a verification email will be sent to the email they provided from dog.bone.vg@gmail.com

## Login
1.	A form to input user details that will allow them to log in
2.	A button that will submit the form.
3.	User can tick the remember me for their information to be saved
4.	If the user inputs an incorrect email or password, then a message will give the user feedback
5.	There is a link to the signup page in case the user doesn't yet have an account

## All Products
1.	User can choose on of the filter methods: by price, by category, or just all products
  a.	by price will show all the shop products sorting by price (low to high); user can change the sorting method with a dropdown option 
  b.	by category will show all the shop products sorting alphabetically (a-z); user can change the sorting method with a dropdown option 
  c.	all products will show all shop's products, default sorting option is not chosen; user can change the sorting method with a dropdown option   

## Dog Food
1.	User can choose on of the categories: dry food, wet food, specialist diets, treats, puppy food or all food
2.	Each category has a page showing items from their category, with information field on top of the page so the user know which category they are browsing; there is a sorting dropdown menu on the top right 

## Dog Equipment
1.	User can choose on of the categories: beds, leads&collars, toys, bowls, crates, grooming
2.	Each category has a page showing items from their category, with information field on top of the page so the user know which category they are browsing; there is a sorting dropdown menu on the top right 

## Dog Wear
1. 	User can choose on of the categories: coats&jackets, fashion, accessories
2.	Each category has a page showing items from their category, with information field on top of the page so the user know which category they are browsing; there is a sorting dropdown menu on the top right 

## Shopping Basket
1.	Users can see the items they added to the basket, with the item details (name, image, price, amount)
2.	Under the item details is a secure checkout button that will take the user to the checkout page and a back to the shop button that will take the user to all items

## Secure Checkout
1.	A form to input user details that will allow them to purchase the items
2.	If a user logged in with their account and provided the delivery information there, the form will be populated by the information from their profile page
3. 	If the user did not fill in the delivery information on their profile page, there is a checkbox that will allow user to save the details they filled on this page to their profile
4. 	Order summary showing all the items user is buying with their details (name, image, price, amount)
5.	Finish order button on the bottom of the page that will finalise the transaction
6. 	Under the finish order button is a red info field showing how much will the user's card be charged for the purchase
7.	If the user input is incorrect, then a message will give the user feedback
8. 	After successful purchase, a pop-up attention box will give user feedback and they will be redirected to a thank you page with the order details
9.	After successful purchase, an email with the order details will be send to the email address the user provided on the form

# Data

I have created my own JSON fixtures files with the categories and products
The categories are: 
- dry food
- wet food
- specialist diets
- treats
- puppy food
- beds
- leads & collars
- toys
- bowls
- crates
- grooming
- coats & jackets
- fashion
- accessories


# Defensive Features

- If a user tries to log out, a confirmation page is displayed, asking them to confirm
- If a user tries to create an account whose username or password does not match the minimum criteria, a message is displayed asking match the format requested
- A new user cannot use the same username as the existing user. If they try this, a message is displayed (username already exists)
- If a user provides an incorrect password, a message is displayed 


# Technologies Used

## Front-end
###### Languages
- [HTML](https://en.wikipedia.org/wiki/HTML)
- [CSS](https://en.wikipedia.org/wiki/CSS)

## Tools & Frameworks
- [Bootstrap](https://getbootstrap.com/docs/4.0/getting-started/introduction/)
- [JavaScript](https://www.javascript.com/)
- [jQuery](https://jquery.com/)
- [Font Awesome](https://fontawesome.com/)
- [Google Fonts](https://fonts.google.com/)

## Back-end Technologies
###### Languages
- [Python](https://www.python.org/)
- [Javascript](https://www.javascript.com/)

###### Tools & Frameworks
- [Django-allauth](https://django-allauth.readthedocs.io/)
- [Django-storages](https://django-storages.readthedocs.io/en/latest/)
- [Stripe](https://stripe.com/)
- [AWS](https://aws.amazon.com/)
- [SQLite](https://stripe.com/)
- [Postgresql](https://www.tableau.com/)
- [Django Cleanup](https://pypi.org/project/django-cleanup/)
- [Django Bootstrap](https://pypi.org/project/django-bootstrap4/)

###### Python & Django  <!-- omit in toc -->
- [Django](https://www.djangoproject.com/)
- [Pillow](https://pillow.readthedocs.io/en/stable/) 
- [boto3](https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html) 
- [botocore](https://pypi.org/project/botocore/)
- [django-allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)
- [django-countries](https://django-allauth.readthedocs.io/en/latest/installation.html)
- [django-phonenumber-field](https://pypi.org/project/django-phonenumber-field/0.2a1/)
- [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/install.html)
- [django-filte](https://django-filter.readthedocs.io/en/stable/)
- [asgiref](https://pypi.org/project/asgiref/1.1.1/)
- [django-environ](https://django-environ.readthedocs.io/en/latest/)
- [django-storages](https://django-storages.readthedocs.io/en/latest/)
- [dj-database-url](https://pypi.org/project/dj-database-url/)
- [unicorn](https://pypi.org/project/django-unicorn/#:~:text=Unicorn%20is%20a%20reactive%20component,or%20re%2Dbuilding%20your%20website)
- [gunicorn](https://pypi.org/project/gunicorn/)
- [oauthlib](https://pypi.org/project/oauthlib/)
- [psycopg2](https://pypi.org/project/psycopg2/)
- [psycopg2-binary](https://pypi.org/project/psycopg2-binary/)
- [requests-oauthlib](https://pypi.org/project/requests-oauthlib/)
- [sqlparse](https://pypi.org/project/sqlparse/)

## Other technologies
- [GitHub](https://github.com/)
- [Heroku](https://heroku.com/)



# Testing

## Basic test
1.	Nav has been fully tested
2.	I have checked that the collapsible open and close appropriately
3.	I have checked buttons enable and disable appropriately
4.	I have checked that the correct form options are unhidden based on the user's previous inputs
5.  I have tested project purchasing as a guest, logged in user and admin
6.	All tests were done on PC and Mobile view


# Deployment

This project was developed on Github, using Gitpod as IDE. It has only master branch. This is pushed and deployed onto Heroku.

## Preparation

 - Install [python 3](https://www.python.org/) on your local environment
 - Install [PIP](https://pip.pypa.io/en/stable/installing/) on your local environment
 - Register with [Git](https://github.com/) if you don't have an account and login before cloning
 - Register with [AWS-S3](https://docs.aws.amazon.com/) if you don't have an account and make sure you can use [S3 Bucket](https://docs.aws.amazon.com/). Create your user group with a policy, attach it to your bucket. Make permission keys ready.
 - Register with [Stripe](https://stripe.com/) if you don't have an account, activate your account, get your API keys ready

## To run this project on your local repository
### Running on Gitpod

This project will be deployed following these steps:

1. Add your own repository on your Github account
2. Click the green 'Gitpod' button on top-right corner of this repo
    (If there isn't a button on your browser, install 'Gitpod' extension on your Chrome browser)

3. Gitpod launches
4. Run the following command (Replace the 'USERNAME' and 'REPO' to your username and repo name):


 ```bash
git remote set-url origin https://github.com/USERNAME/REPO.git

```
5. Run this command below to install all the modules on requirements.txt file:

 ```bash
pip3 install -r requirements.txt

```
6. Create these environment variables:

| Config Vars      | Value |
|:------------- |:------------- |
| AWS_ACCESS_KEY_ID | your_value | * https://console.aws.amazon.com
| AWS_SECRET_ACCESS_KEY | your_value | * https://console.aws.amazon.com
| DATABASE_URL | your_value | * Your Postgres database URL
| EMAIL_HOST_PASS | your_value | 
| EMAIL_HOST_USER | your_value | 
| SECRET_KEY | your_value | *https://djecrety.ir
| STRIPE_PUBLIC_KEY | your_value | *https://dashboard.stripe.com/test/apikeys
| STRIPE_SECRET_KEY | your_value | *https://dashboard.stripe.com/test/apikeys
| STRIPE_WH_SECRES | your_value |   *https://dashboard.stripe.com/test/apikeys
| USE_AWS | your_value |    * https://console.aws.amazon.com

7. Replace your_value with your values

8. On your CLI, run this code below to test migration

```bash

python3 manage.py migrate --plan

```

9. If there was any errors, find out solutions on [Python's documentation](https://docs.djangoproject.com/en/3.1/ref/django-admin/)
   If there was no issues found, run this code below:


```bash

python3 manage.py migrate 

```
10. If there was any errors, find out solutions on [Python's documentation](https://docs.djangoproject.com/en/3.1/ref/django-admin/)
    If there was no issues found, run this code below to create a superuser (Your admin account). 

```bash

python manage.py createsuperuser

```

11. Run this code to run server on local :

```bash

python manage.py runserver

```
12. If no errors, the CLI will provide the link to the local server. Click on the link to open the website.

13. Go to https://your-local-url.com/admin to find out your superuser login is working.

### Running on your local environment (PC/Mac)

1. On top-righ corner of this page, find 'Code' button to open a dropdown list of links. Download zipped files into your local folder. Alternatively, navigate to your chosen folder on your CLI and run this command:

```bash

git clone https://github.com/machikolacey/composermlacey

```

2. In your chosen IDE, open the folder


3. Create a virtual environment to load these packages.
Please see [Python's official documentation](https://www.python.org/) for more details.

4. Run these commands to create your virtual environment:
Please see [Python's official  documentation](https://docs.python.org/3/library/venv.html) for more details.

```bash

py .venv venv

```

```bash

source venv/Scripts/activate


```
5. Run this command below to install all the modules on requirements.txt file:

 ```bash

pip3 install -r requirements.txt

```
6. In the root of your project, create a file 'env.py' abd add environmental variables. The format will be like this below:


 ```bash

import os

os.environ["VARIABLE_NAME"] = "YOUR_VALUE"

```

7. Add 'env.py' onto your .gitignore file.


8. Replace your_value with your values

| Config Vars      | Value |
|:------------- |:------------- |
| AWS_ACCESS_KEY_ID | your_value | * https://console.aws.amazon.com
| AWS_SECRET_ACCESS_KEY | your_value | * https://console.aws.amazon.com
| DATABASE_URL | your_value | * Your Postgres database URL
| EMAIL_HOST_PASS | your_value | 
| EMAIL_HOST_USER | your_value | 
| SECRET_KEY | your_value | *https://djecrety.ir
| STRIPE_PUBLIC_KEY | your_value | *https://dashboard.stripe.com/test/apikeys
| STRIPE_SECRET_KEY | your_value | *https://dashboard.stripe.com/test/apikeys
| STRIPE_WH_SECRES | your_value |   *https://dashboard.stripe.com/test/apikeys
| USE_AWS | your_value |    * https://console.aws.amazon.com



9. On your CLI, run this code below to test migration

```bash

python3 manage.py migrate --plan

```

10. If there was any errors, find out solutions on [Python's documentation](https://docs.djangoproject.com/en/3.1/ref/django-admin/)
   If there was no issues found, run this code below:


```bash

python3 manage.py migrate 

```
11. If there was any errors, find out solutions on [Python's documentation](https://docs.djangoproject.com/en/3.1/ref/django-admin/)
    If there was no issues found, run this code below to create a superuser (Your admin account). 

```bash

python manage.py createsuperuser

```

12. Run this code to run server on local:

```bash

python manage.py runserver

 ```

13. If no errors, the CLI will provide the link to the local server. Click on the link to open the website.

14. Go to https://your-local-url.com/admin to find out your superuser login is working.

## Remote Deployment (Run the project on Heroku.com)

If you want to add it to your Heroku account, follow the instructions below:

1. Add an app for this project
2. Create an AWS S3 bucket, create access group and attach access policy.
3. Back to your Heroku app, the 'Settings' tab on your app, add Config variables:

| Config Vars      | Value |
|:------------- |:------------- |
| AWS_ACCESS_KEY_ID | your_value | * https://console.aws.amazon.com
| AWS_SECRET_ACCESS_KEY | your_value | * https://console.aws.amazon.com
| DATABASE_URL | your_value | * Your Postgres database URL
| EMAIL_HOST_PASS | your_value | 
| EMAIL_HOST_USER | your_value | 
| SECRET_KEY | your_value | *https://djecrety.ir
| STRIPE_PUBLIC_KEY | your_value | *https://dashboard.stripe.com/test/apikeys
| STRIPE_SECRET_KEY | your_value | *https://dashboard.stripe.com/test/apikeys
| STRIPE_WH_SECRES | your_value |   *https://dashboard.stripe.com/test/apikeys
| USE_AWS | your_value |    * https://console.aws.amazon.com

6. Replace your_value with your values

7. On your CLI, run this code below to test migration

```bash

python3 manage.py migrate --plan

```

8. If there was no errors, run this code below to migrate database:

```bash

python3 manage.py migrate 

```

9. If there was any errors, find out solutions on [Python's documentation](https://docs.djangoproject.com/en/3.1/ref/django-admin/)
   If there was no issues found, run this code below to create a superuser (Your admin account). 

```bash

python manage.py createsuperuser

```

10. Go back to your Gitpod workspace, run this code below for the first deployment on Heroku:

```bash
    git init
    git commit -m 'First commit for Heroku deployment'
    git push -u origin
``` 

11.  On your Heroku app, click on the "Deploy" tab, in 'Deployment method' select GitHub.

12. Find your Github repository and click on it to connect to your repo.

13. In "Manual deploy" section, make sure your repo branch is chosen, click on "Deploy Branch".

14. In "Automatic deploys" section, enable automatic deploy, if you choose to.

15. On the top-right corner on the app page, find "Open App" button to open your app.

16. Go to https://your-app-name-herokuapp.com/admin to find out your superuser login is working.


# Credit

I mostly based my project on the tutorials provided by the Code Institute Data Centric Development Mini Project

Additional resources: 
-	https://pythonise.com/series/learning-flask/flask-session-object 
-	https://animate.style/ 
-	Wallpaper was downloaded from https://wallpapercave.com/wp/wp5619654.jpg
-	https://www.w3schools.com/tags/att_input_pattern.asp#:~:text=The%20pattern%20attribute%20specifies%20a,pattern%20to%20help%20the%20user

# Acknowledgements



