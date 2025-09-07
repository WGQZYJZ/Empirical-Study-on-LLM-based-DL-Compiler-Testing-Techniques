The inputs to the model are 10 x 4 x 500 tensors. The expected output is a 10 x 1 tensor with values greater than or equal to zero and smaller than one. This model can be trained as follows:


# Description of requirements
Please include any specific notes in this section that you know are required for the submission.
# Submission instructions
You need to complete this assignment by submitting a Python file to `submit` on Moodle. Please keep the following content at the beginning of your submit script (the name of which is listed in the top left corner):
You are not allowed to use any third-party libraries in your submission. You should implement only the necessary functions (the `imread` function is already written for you). Please also keep track of the time taken by your script (e.g., 36.5 sec) and any other useful information about the performance of your model. If you feel like there are too many files to upload, please split them into multiple parts in Moodle or ZenHub.

If you have already used PyTorch and used PyTorch for machine learning before, please do not use this project as an inspiration. The purpose is only to reinforce basic concepts of PyTorch, which has been used by other students so far. Your submission must meet the requirements listed below:
- In the `__init__` method, construct a neural network with a specified number of layers (for example, 4 in our case). The architecture will not be fixed; your model must work on any input. Please take note of the number of parameters and compute time taken by the optimizer to decide which model has better performance.
- The `forward` method is used for computing the output of the network. It should contain the necessary code that performs the following tasks:
  1. Read in an image file using torchvision, using `imread(filename)`. For simplicity, you are not allowed to use any third-party libraries in your submission. You need to implement only the necessary functions (the `imread` function is already written for you).
  2. Apply the following transformations to the input tensor:
    1. Rescale the image from range [0, 255] to range [-1, 1]. For example, a value of 255 represents an input pixel with intensity -1 and a value of 0 represents zero, which should be converted into one-pixel (-1) by `transform(img)`.
  3. Perform the forward pass to get an output tensor, which is equal to the input multiplied by `alpha`. Please use torch.mul instead of numpy multiplication.
  4. The result of your model should be returned in range [0, 1]. For example, a value of -0.5 represents an input pixel with intensity -0.5 and a value of 0.5 represents zero, which should be converted into one-pixel (-0.5) by `transform(img)`.
