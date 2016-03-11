cd /etc/nginx/sites-enabled/ 
sudo rm default
sudo ln -s /home/box/web/etc/nginx.conf test.conf
sudo chmod +rx /var/log/nginx
sudo pip3 install django
sudo apt-get remove gunicorn
sudo pip3 install gunicorn
sudo apt-get install python3-dev libmysqlclient-dev
sudo pip3 install mysqlclient 

sudo /etc/init.d/nginx start
cd ~/web/ask/
#gunicorn -c ../etc/gunicorn.conf --access-logfile ../log2.txt --error-logfile ../log.txt --log-level debug ask.wsgi


