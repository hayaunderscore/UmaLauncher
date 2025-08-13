cd ./umalauncher
set PYTHONPATH=set PYTHONPATH=%CD%\external
python -m nuitka threader.py
cd ..