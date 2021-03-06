# russian-troll-detector
A system that returns the likelihood of a given Twitter account to be a Russian troll.

## Related work
[Still Out There: Modeling and Identifying Russian Troll Accounts on Twitter](https://arxiv.org/pdf/1901.11162.pdf)

There  is  evidence  that  Russia’s  Internet  Research  Agency attempted  to  interfere  with  the  2016  U.S.  election  by  running fake accounts on Twitter—often referred to as “Russian trolls”. In this work, we: 1) develop machine learning models
that predict whether a Twitter account is a Russian troll within a set of 170K control accounts; and, 2) demonstrate that it is possible to use this model to find active accounts on Twitter still likely acting on behalf of the Russian state.

## How to build
**1.Clone the repository.**
```
git clone https://github.com/trusttri/russian-troll-detector.git
```

Or if you clone from your forked one,
```
git clone https://github.com/[YOUR USERNAME]/russian-troll-detector.git
```

**2.Install [virtualenv](https://virtualenv.pypa.io/en/latest/)**
```
pip3 install virtualenv
```

**3.Create & activate your virtualenv and install the needed python packages.**

Go to russian-troll-detector/ 
```
cd russian-troll-detector/
```

Create a virtualenv. You may name it as you wish, here we use "rtenv (russian troll env)"

*(Note: Built with python 3.7. If you use a different version and find issues, please ping us!)*

```
virtualenv -p python3.7 rtenv
```

Activate the virtualenv
```
source rtenv/bin/activate
```
Now you will see your terminal like the following:
```
(rtenv) ~$
```

Install the needed python packages. Everything including Django is included in [requirements.txt](russian-troll-detector/russian_troll_detector/requirements.txt) so just run the following.
```
(rtenv) ~$ pip install -r requirements.txt
```

**4.Run the server**
```
(rtenv) ~$ python manage.py runsever
```
Visit [http://localhost:8000/](http://localhost:8000/)
