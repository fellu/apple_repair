Mobile / Apple device repair management system
==============================================
This software is build to make client devices repair and inventory management more systematic.

Idea is that you can connect device to workstation and it will pull all the relevant information about device.
eg. Model, battery data, serial number, and other needed stuff.

After adding device to database, you can print qr code label with minimal to device, after that device can be scanned when more information is needed to add.

With the collected data you can check what spare parts is needed and also can generate files like binary file for true tone repair, without original screen being availale.

Implemented:
 - Basic Django functionality. :P

Partially implemented
 - Python wrapper for idevice

Not implemented:
 - Device management
 - Client management
 - Inventory management
 - True tone binary file generation


.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
     :target: https://github.com/ambv/black
     :alt: Black code style


:License: MIT

