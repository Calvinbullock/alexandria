# Overview

Alexandria is a basic file storage web app built with django. The purpose is to learn the basics of Django and get experience building 
a backend that handles file storage and serving. Also to learn how to use Django for other projects.

To start the server:
- git clone repo
- cd into alexandria root
- run $ python3 manage.py runserver
- go to http://127.0.0.1:8000/alexandria_app/index/

{Provide a link to your YouTube demonstration.  It should be a 4-5 minute demo of the software running (starting
    the server and navigating through the web pages) and a walkthrough of the code.}

# Useful commands
- python3 manage.py runserver (start server)
- python3 manage.py makemigrations
- python3 manage.py migrate

[Software Demo Video]()

# Web Pages

index page is there to let you upload files, (only images currently.)
list-files is there to list all the uploaded files.

# Development Environment

IDEs / editers: Neovim and VS code.
language/frameworks/libraries: HTML, CSS, python, Django.

# Useful Websites

{Make a list of websites that you found helpful in this project}
* [Django file uploads documentation](https://docs.djangoproject.com/en/5.0/topics/http/file-uploads/)
* [Django file managment](https://docs.djangoproject.com/en/5.0/topics/files/)
* [Video tuturial on working with files](https://www.youtube.com/watch?v=lKyH_ZGtvwM)

# Future Work

{Make a list of things that you need to fix, improve, and add in the future.}
* Upload and serve more then jsut images.
* set up a more production ready system: see this link for more details:
        https://docs.djangoproject.com/en/5.0/howto/static-files/#serving-files-uploaded-by-a-user-during-development
* Better styling, all css styling is very bare bones.


