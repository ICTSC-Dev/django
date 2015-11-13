rm -rf db.sqlite3
rm -rf Account/migrations
rm -rf Log/migrations
rm -rf Notice/migrations
rm -rf Problems/migrations

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
