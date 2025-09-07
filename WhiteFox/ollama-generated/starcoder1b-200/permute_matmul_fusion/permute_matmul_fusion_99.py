# Testing the generated code

1. Run `python codegen_tester.py` with the above `.py` file as input and the following parameters:
    - The generated PyTorch model should be saved in `generated_model.py`.

2. Import `generated_model.py` into your Python project.
3. Invoke the class' method `generate_input_tensor()`.

4. Run the test function with the below parameters:
    - For the input tensor: `torch.randn(1, 5, 3, 2)`.
    - For the model's output tensor: `__output__`.
    - The test result should match the specified requirements in `.txt` file:
    - If all tests are successful, you will see the below output printed to console:
