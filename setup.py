from setuptools import setup, find_packages

setup(
    name="pp-adjuster",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'pp-adjuster=script:main',  # Adjust the module and function name as necessary
        ],
    },
    author="Aly Raffauf",
    author_email="aly@raffauflabs.com",
    description="Automatically adjust power profile and notify user.",
    license="GPL",
)
