

# Requirements for PyTorch integration
- You must write a unit test for each class and function that you are writing. This can be done by copying the code from `test/test_models.py` file into `tests/unit/<function name>.py` and adding a corresponding entry in `tests/requirements.txt`. In this way, you can run a unit test to check if your changes to the model are working correctly.
- To execute each unit test, please make sure you have installed the package in the virtualenv with the command `pip install -r requirements.txt` on your system. After that, the following commands will be enough to run all tests in the package:
