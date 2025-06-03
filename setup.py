from setuptools import setup, find_packages
from datetime import datetime

current_year = datetime.now().year

AUTHOR_INFO = f"""/**
 * Anubhab Anjan
 *
 * @author Anubhab Anjan
 * @copyright 2025-{current_year}
 * @mail  me@anubhabanjan.com
 * @telegram Anubhab Anjan  <t.me/ANUBHAB_ANJAN>
 */
"""

setup(
    name="readme-md-generator",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "click",
        "jinja2",
    ],
    entry_points={
        "console_scripts": [
            "generate-readme=readme_md_generator.cli:main",
        ],
    },
    author="Anubhab Anjan",
    author_email="me@anubhabanjan.com",
    description="An ultimate GitHub README.md generator",
    long_description=open("README.md", encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/anubhabanjan/readme-md-generator",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_data={
        'readme_md_generator': ['templates/*.md'],
    },
)
