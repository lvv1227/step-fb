mysql -uroot -e "CREATE DATABASE IF NOT EXISTS my_django_db";    
mysql -uroot -e "CREATE USER 'leonid'@'localhost' IDENTIFIED BY '12345'";  
mysql -uroot -e "GRANT ALL ON my_django_db.* TO 'leonid'@'localhost'";  


#-p'12345'
