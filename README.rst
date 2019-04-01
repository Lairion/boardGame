==============
Board game
==============

---------------

* `Installation`_
* `Usage`_

---------------

============
Installation
============

Clone the repo and install:

.. code-block:: bash

    $ git clone https://github.com/Lairion/boardGame.git
    $ cd boardGame
    $ pip install -r requirements.txt

Make superuser:

.. code-block:: bash

   $ python manage.py createsuperuser

-----------------

=====
Usage
=====

To use the game you need to run server. Use next command for that:  

.. code-block:: bash

   $ python manage.py runserver

Than login on server by this endpoint:

    http://<host_name>/admin/login/

Next, open browser and input this endpoint:

    http://<host_name>/rooms/

For create game's room: 

 - Click on "Add room" button;

 - In open modal window, input data;

 - Click on "Run" button.

Than, you can see more information if you click on "All detail", or delete the room if you click on "Delete" 
