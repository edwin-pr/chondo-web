# settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_mysql_username',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'your_mysql_host',  # Typically 'localhost' or '127.0.0.1'
        'PORT': 'your_mysql_port',  # Default MySQL port is usually 3306
    }
}
