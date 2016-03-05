cd ~/web/ask/
gunicorn -c ../etc/gunicorn.conf --access-logfile ../log2.txt --error-logfile ../log.txt --log-level debug ask.wsgi

