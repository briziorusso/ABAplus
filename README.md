# ABAplus 

http://www-abaplus.doc.ic.ac.uk/

## Maintenance

1. Get on Imperial's network (e.g. SSH to [shell](shell3.doc.ic.ac.uk))
2. `ssh vm-www-abaplus.doc.ic.ac.uk`
3. `ksu`
4. Login to get root rights
5. `cd /aba_plus/aba_plus`

To restart server:
1. Find the gunicorn process IDs `ps ax|grep gunicorn`
2. Terminate the first two processes one by one `kill ID`
3. To check for operational errors, run the gunicorn in the terminal `gunicorn aba_plus.wsgi`
4. Once the issues are fixed, kill the gunicorn and run as daemon `gunicorn -D aba_plus.wsgi`

To update from the [abaplus gitlab repo](https://gitlab.doc.ic.ac.uk/clarg/aba_plus), simply `git pull`

## Requirements

Web app works with 
* Python 3
* Django 2.2
* clingo 4.5.4 https://sourceforge.net/projects/potassco/files/clingo/4.5.4/
* DLV 2012-12-17 http://www.dlvsystem.com/dlv/

---

`stable.py` (together with auxil.py) is a separate module for computing <-stable extensions of flat ABA+ frameworks. 
(Needs neither Django nor DLV.)

```python stable.py```

