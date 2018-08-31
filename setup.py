import setuptools


with open('readme.md') as readme_file:
    readme = readme_file.read()


setuptools.setup(
    name='BulletTrainAPI',
    version='1.1.0',
    description='Python REST API for Bullet-Train. Ship features with confidence using feature '
                'flags and remote config. Host yourself or use our hosted version at '
                'https://bullet-train.io/ https://bullet-train.io/',
    long_description=readme,
    package_dir={"": "src/"},
    packages=[
        'api',
        'api.migrations',
        'app',
        'docs',
        'docs.migrations',
        'users',
        'users.migrations',
        'features',
        'features.migrations',
        'projects',
        'projects.migrations',
        'environments',
        'environments.migrations',
        'organisations',
        'organisations.migrations',
    ],
    classifiers=[
        'Development Status :: 1',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    author='Solid State Group',
    author_email='projects@solidstategroup.com',
    url='https://bullet-train.io/',
    install_requires=[
        'appdirs',
        'django-cors-headers',
        'djangorestframework',
        'gunicorn',
        'pyparsing',
        'requests',
        'six',
        'whitenoise',
        'dj-database-url',
        'drf-nested-routers',
        'shortuuid',
        'django-rest-auth',
        'django-allauth',
        'sendgrid-django',
        'psycopg2-binary',
        'coreapi',
        'django-rest-swagger',
        'Django',
        'numpy',
    ],
)
