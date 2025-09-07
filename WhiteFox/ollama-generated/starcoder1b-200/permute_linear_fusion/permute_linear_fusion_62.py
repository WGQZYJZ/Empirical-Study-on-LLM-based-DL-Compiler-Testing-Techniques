This is a sample of an invalid model:
This model works in C++, but cannot be converted to Python due to Python's `staticmethod` keyword restriction. Therefore, it will not run.

# Requirements
The model should meet one of these requirements:
- [ ] Can run on a CPU with CUDA
- [ ] Can run on a CPU without CUDA (CUDA support will be automatically enabled by Cython if available)
- [ ] Should run and pass the test cases (test scripts have been provided for both the CPU and GPU to check if it is supported, in case the GPU is unavailable, only the CPU tests are run; you can use other options as well)
  - Please add comments on your solution and give a reason for why it cannot work on a CPU with CUDA, on CPU without CUDA or any unsupported OS.

# Test
Please add your test cases to `tests/` directory and make sure that the test case names are correct. If you add new tests for an existing algorithm, please also add them to the corresponding folder in the same level as the test case in which it is used. The input data should be added into a pickle file at `tests/data`, so the model can be run on these test cases by using `pytest` command:
If you are not sure about how to write tests, please use this guide [How To Write a Good Test Case](https://realpython.com/how-to-write-a-good-unit-test/) for general knowledge and [How to Write Tests with pytest](https://www.freecodecamp.org/news/how-to-write-tests-with-pytest-f6572c010c48/).

# Author
<NAME>
