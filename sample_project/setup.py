try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Example Python Project',
    'author': 'Horace Williams',
    'url': 'worace.works',
    'download_url': 'worace.works',
    'author_email': 'horace@worace.works',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['sample'],
    'scripts': [],
    'name': 'sample'
}

setup(**config)
