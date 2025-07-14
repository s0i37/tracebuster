from distutils.core import setup

setup(
  name = 'tracebuster',
  version = '1.0.3',
  description = 'fast tracing networks tool and finding live subnets',
  author = 's0i37',
  author_email = 's0i37@yahoo.com',
  url = 'https://github.com/s0i37/tracebuster',
  keywords = ['traceroute', 'reconnaissance'],
  classifiers = [],
  scripts=['bin/tracebuster'],
  install_requires=[
    'scapy',
    'netaddr',
    'pydot'
  ]
)
