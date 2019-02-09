# russian-troll-detector
A system that returns the likelihood of a given Twitter account to be a Russian troll.

## Publications
https://arxiv.org/pdf/1901.11162.pdf

There  is  evidence  that  Russia’s  Internet  Research  Agency attempted  to  interfere  with  the  2016  U.S.  election  by  running fake accounts on Twitter—often referred to as “Russian trolls”. In this work, we: 1) develop machine learning models
that predict whether a Twitter account is a Russian troll within a set of 170K control accounts; and, 2) demonstrate that it is
possible to use this model to find active accounts on Twitter still likely acting on behalf of the Russian state.

## How to build
**1.Install [virtualenv](https://virtualenv.pypa.io/en/latest/)**
```
pip3 install virtualenv
```

**2.Create a virtualenv and install the python packages specified in requirements.txt**

Create a virtualenv. You may name it as you wish, here we use "rtenv (russian troll env)"
```
virtualenv -p python3.7 rtenv
```
*[ Note: Built with python 3.7. If you use a different version and find issues, please ping us! ]*

Activate the virtualenv
```
source rtenv/bin/activate
```
Install the needed python packages
```
pip install -r requirements.txt
```

**3.Run the server**
```
python manage.py runsever
```
Visit [http://localhost:8000/](http://localhost:8000/)
