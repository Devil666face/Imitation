python -m venv venv
.\venv\Scripts\pip.exe install --no-index --find-links .\pkg\ -r .\requirements.txt
.\venv\Scripts\python.exe manage.py collectstatic --no-input
rem .\venv\Scripts\python.exe manage.py migrate
rem .\venv\Scripts\python.exe manage.py createcachetable
