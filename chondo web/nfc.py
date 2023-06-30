# settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mydb',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',  # Typically 'localhost' or '127.0.0.1'
        'PORT': 3306,  # Default MySQL port is usually 3306
    }
}
