from setuptools import find_packages , setup

setup(
    name = 'Food OrderBot',
    version = '0.0.1',
    author = 'Soura',
    author_email = 'souradeeproy.10@gmail.com',
    packages = find_packages(),
    install_requires = ["chainlit","notebook","ipywidgets","tqdm","python-dotenv","langchain-google-genai"]
)