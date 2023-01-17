set "HasArgument="
for %%a in (%*) do if /i "%%~a"=="-venv" set HasArgument=true
if defined HasArgument (
  echo Create venv from local python
  python -m venv venv
) else (
  echo Create venv from source files
  .\Python38\python -m venv venv
)
.\venv\Scripts\pip.exe install --no-index --find-links .\pkg\ -r .\requirements.txt
.\venv\Scripts\python.exe manage.py collectstatic --no-input
rem .\venv\Scripts\python.exe manage.py migrate
rem .\venv\Scripts\python.exe manage.py createcachetable
