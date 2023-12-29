from setuptools import setup, find_packages

setup(
    name='KPI Assignment',
    version='0.1.0',
    author='Nicolò Santamaria',
    description='API for computing various types of KPI values and plots',
    packages=find_packages(),  # Automatically discover and include all packages
    install_requires=[
        'flask',
        'matplotlib',
    ],
    entry_points={
        'console_scripts': [
            'kpi = kpi.main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
