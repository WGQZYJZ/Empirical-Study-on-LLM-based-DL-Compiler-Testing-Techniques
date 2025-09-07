The function `conv_transpose` and `clamp_min` are provided for you in case the above pattern does not satisfy your requirements. In that case, we will provide you with the following models:
## Test on test.py and check result
Please use the test.py to check your code. We provide you with three examples of generated model for you:
* `Conv` and `ConvTranspose`: These two models generate the same output but in different form. The input dimension is always 3, and the number of output channels is always 8. The input data for the test program is the following:
* `ReLU`: This model generates the output for which $0 < \alpha < 1$. The input data for this program is the following:
* `ERF`: This model generates the output for which $0 \le f(\alpha) < 1$. The input data for this program is the following:


# References
[1] https://pytorch.org/docs/stable/torchvision/models.html?highlight=conv2d#torchvision.models.resnet18
