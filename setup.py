from setuptools import setup

setup(
	name='click-trial',
	version='1.0',
	py_modules=['trial'],
	install_requires=[
		'Click',
	],
	entry_points='''
		[console_scripts]
		trial=trial:cli
	''',
)
