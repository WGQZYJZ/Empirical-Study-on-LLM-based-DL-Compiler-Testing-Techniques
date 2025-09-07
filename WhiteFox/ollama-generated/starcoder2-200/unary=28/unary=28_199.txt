

import torch  # noqa: E402
 
class Model(torch.nn.Module):
    def __init__(self, inputSize = 835, outputSize = 17986, hiddenSize = 53):
        super().__init__()
        self._conv1 = torch.nn.Conv2d(in_channels=inputSize, out_channels=outputSize, kernel_size=(hiddenSize), padding=(0,), bias=True) # noqa: E501
 
    def forward(self, x):  # noqa: E9003
        return self._conv1(x).sum()

# Initializing the model
m = Model()

# Inputs to the model
