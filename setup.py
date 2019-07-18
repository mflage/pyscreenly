from distutils.core import setup
setup(
  name = 'pyscreenly',
  packages = ['pyscreenly'],
  version = '0.1',
  license='MIT',
  description = 'Python library to use the Screenly OSE API',
  author = 'Marius Flage',
  author_email = 'marius@flage.org',
  url = 'https://github.com/mflage/pyscreenly',
  download_url = 'https://github.com/mflage/pyscreenly/archive/v_01.tar.gz',
  keywords = ['screenly'],
  install_requires=[
          'requests',
      ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 3',
  ],
)
