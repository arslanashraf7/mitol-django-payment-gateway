
# DO NOT EDIT THIS FILE -- AUTOGENERATED BY PANTS
# Target: src/mitol/payment_gateway:mitol-django-payment-gateway

from setuptools import setup

setup(**{
    'authors': [
        'MIT Office of Open Learning <mitx-devops@mit.edu>',
    ],
    'classifiers': [
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    'description': 'Django application to handle payment processing',
    'install_requires': (
        'cybersource-rest-client-python>=0.0.36',
        'django<4.0,>=2.2.12',
        'mitol-django-common~=2.4.0',
        'setuptools',
    ),
    'license': 'BSD 3-Clause License',
    'name': 'mitol-django-payment-gateway',
    'namespace_packages': (
        'mitol',
    ),
    'package_data': {
        'mitol.payment_gateway': (
            'CHANGELOG.md',
            'README.md',
            'py.typed',
        ),
    },
    'packages': (
        'mitol',
        'mitol.payment_gateway',
        'mitol.payment_gateway.settings',
    ),
    'version': '1.5.0',
    'zip_safe': True,
})
