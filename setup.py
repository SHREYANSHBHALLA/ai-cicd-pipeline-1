from setuptools import setup, find_packages

setup(
    name='ai-cicd-pipeline',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A CI/CD pipeline for testing and deploying AI agents',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'Flask==2.0.1',
        'pytest==6.2.4',
        'requests==2.26.0',
        'pandas>=1.5.0',
        'numpy>=1.23.0',
        'scikit-learn>=1.1.0',
        'matplotlib>=3.5.0',
        'dash==2.0.0',
        'gunicorn==20.1.0',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)