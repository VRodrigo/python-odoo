=============
Odoo Contacts
=============

Instalation
===========

Is required to install python's library "email_validator" in order to
get this module working.

pip3 install email_validator

Usage
=====

#. Go to *Contacts* to see your contact list.
#. Click on upload contact to load new contacts through and XML.

An example of XML is:

<?xml version='1.0'?>
<data>
   <contact>
      <firstname>??????????</firstname>
      <lastname>???????????</lastname>
      <address>?????? ?????? ??</address>
      <email>?????@?????.???</email>
      <phone>+?? ?? ??? ?? ??</phone>
    </contact>
</data>

There is an XML example in example/contact.xml too.

Credits
=======

Authors
~~~~~~~

* Victor Rodrigo

Maintainers
~~~~~~~~~~~

This module is maintained by Victor Rodrigo.
