wadllib-example
===

Example of wadllib based on the python.org tutorial

Activate virtualenv
---

virtualenv env
source env/bin/activate

Install automatic
---

pip install -r requirements.txt


Download for manual install
---
wget https://launchpad.net/wadllib/trunk/1.3.2/+download/wadllib-1.3.2.tar.gz

tar xvf wadllib-1.3.2.tar.gz
cd wadllib-1.3.2
python setup.py build
python setup.py install 

Run example and enjoy the comments
---

python example.py


Navigate HTTP resources using WADL files as guides.

wadllib should work with Python >= 2.4.
