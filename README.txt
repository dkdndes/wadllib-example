wadlib example
===

Install automatic
---

pip install -r requirements.txt


Download for manual install
---
wget https://launchpad.net/wadllib/trunk/1.3.2/+download/wadllib-1.3.2.tar.gz


Install manual
---

Note: Installation should take place in a isolated environement.

virtualenv env
source env/bin/activate
tar xvf wadllib-1.3.2.tar.gz
cd wadllib-1.3.2
python setup.py build
python setup.py install 

# On a linux, bsd, mac os x environment 
ln -s wadllib-1.3.2 wadlib


Navigate HTTP resources using WADL files as guides.

wadllib should work with Python >= 2.4.
