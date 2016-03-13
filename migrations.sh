cd /home/box/web/ask/qa/migrations/
rm *
cd /home/box/web/ask/
python3 manage.py makemigrations qa
python manage.py sqlmigrate qa 0001
python3 manage.py migrate
