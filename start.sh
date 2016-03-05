cd /etc/nginx/sites-available/
sudo rm default
sudo ln -s /home/box/web/etc/nginx.conf test.conf

pip3 install django
sudo apt-get uninstall gunicorn

