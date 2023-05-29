import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_desc = f.read()

__version__ = "0.0.1"

REPO_NAME = "TEXT_SUMMARIZER"
AUTHOR = "steve-mir"
SRC = "textSummarizer"
EMAIL = "ekechukwuemeka25@gmail.com"

setuptools.setup(
    name=SRC,
    version=__version__,
    author=AUTHOR,
    author_email=EMAIL,
    description="A Text Summarizer using NLP",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)