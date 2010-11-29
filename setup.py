from setuptools import setup, find_packages



setup(name = 'django-account',
      version = '0.1',
      description = 'Account handling for django projects, extends django-registration and django-profile',
      author = 'Leander Hanwald',
      author_email = 'shockflash@web.de',

      url = 'https://github.com/shockflash/account/',
      download_url = 'https://github.com/shockflash/account/tarball/master',

      packages = find_packages(),

      license = 'BSD',

      classifiers = ['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Software Development :: Libraries :: Python Modules',
                   'Topic :: Utilities'],
      )

