from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

REQUIREMENTS = ["numpy>=1.18.4", "pandas>=1.0.3", "changeo>=1.0.0", "anndata>=0.7.1", "scanpy>=1.4.6", "scrublet>=0.2.1", "python-Levenshtein>=0.12.0", "distance>=0.1.3", "joblib>0.14.1", "scikit-learn>0.23.0", "scipy>=1.4.1", "numba>0.48.0", "pytables>3.6.1", "seaborn>0.10.1", "python-igraph>0.8.2", "networkx>=2.4", "leidenalg>=0.8.0"]
setup(
    name="sc-dandelion",
    version="0.0.1",
    author="zktuong",
    author_email="kt16@sanger.ac.uk",
    description="sc-BCR analysis tool",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/zktuong/dandelion/",
    packages=find_packages(),
    install_requires=REQUIREMENTS,
    include_package_data=True,
    scripts=['bin/blastn', 'bin/igblastn', 'bin/makeblastdb', 'bin/tigger-genotype.R'],
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
    ],
    
)
