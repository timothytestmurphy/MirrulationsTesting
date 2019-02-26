This repository currently has a single pytest.

To use this repository, first fork and clone or clone.

Then, make a virtual environment with `python3 -m venv .env'

Enter the environment with `source .env/bin/activate`

Run `pip install -r requirements.txt`

Run `pip install -e .`

You can now run `pytest` and ensure that tests are passing.

The point of this repository is to test out pull requests and enable continuous integration.
The current plan is to use TravisCI, and make sure that pytest can be automatically run, 
eventually setting up the ability to have TravisCI use auth keys or passwords that are hidden 
that would be emulating running the project on a local machine. This will be implemented on 
Moravian College's Mirrulations project. This repo may also be used to test out fakeredis, and
have TravisCI implement that for testing as well.
