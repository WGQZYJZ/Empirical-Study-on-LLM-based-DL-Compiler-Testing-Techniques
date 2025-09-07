conv = Conv2d(3072, 1024)
linear = Linear(785, 6, bias=True) # Applying linear transformation to the input tensor with bias. Note that the number of input features is equal to `785` and not necessarily the same as before, which may vary for each model generated based on the original model.
lrelu = LeakyReLU(0.1)  # ReLU with a slope of `0.1`.
bn2d = BatchNorm2D()  # Applying batch normalization operation to the input tensor.
dropout = Dropout()  # Applying dropout operation to the input tensor.
relu6 = Relu6() # Applying ReLU6 operation to the input tensor.
maxpool3x3 = MaxPool2d(kernel_size=3, stride=1, padding=0) # Applying max pooling with kernel size `3`, stride of 1, and a padding of 0. Note that the padding may vary for each model generated based on the original model.
dropout2d = Dropout2D()  # Applying dropout operation to the input tensor.
maxpool5x7 = MaxPool2d(kernel_size=7, stride=1, padding=3)  # Applying max pooling with kernel size `5` and a padding of `3`. The padding may vary for each model generated based on the original model.

