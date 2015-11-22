This tutorial attempts to explain Celery + RabbitMQ to a beginner, with working code.

To compile the talk.tex file on Ubuntu, use:

.. code-block:: console

    $ sudo apt-get install texlive-full
    $ sudo apt-get install python-pygments
    $ pdflatex -shell-escape talk.tex && evince talk.pdf

To install dependencies:

.. code-block:: console

    $ sudo xargs apt-get install -y < apt-gets.txt
    $ pyvenv .
    $ . bin/activate
    $ pip3 install -r requirements.txt

To run the django examples use the standard boilerplate:

.. code-block:: console

    $ cd django_example
    $ ./manage.py makemigrations
    $ ./manage.py migrate
    $ ./manage.py collectstatic
    $ ./manage.py runserver

Visit at `127.0.0.1:8000`.
