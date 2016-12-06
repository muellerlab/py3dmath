from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='py3dmath',
      version='0.0.1',
      description='Python py3dmath library',
      long_description='TODO',
      url='http://github.com/muellerlab/py3dmath',
      download_url = 'https://github.com/muellerlab/py3dmath/archive/0.1',
      author='Mark W. Mueller',
      author_email='mwm@mwm.im',
      license='GPL V3',
      packages=['py3dmath'],
      zip_safe=False,
      classifiers=[],
      tests_require=['cvxpy'],
      )
