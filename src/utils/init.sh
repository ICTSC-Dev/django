rm -rf db.sqlite3
#rm -rf pjama/account/migrations
#rm -rf pjama/log/migrations
#rm -rf pjama/notice/migrations
#rm -rf pjama/problem/migrations


python manage.py makemigrations account
python manage.py makemigrations log
python manage.py makemigrations notice
python manage.py makemigrations problem
python manage.py migrate
python manage.py createsuperuser


