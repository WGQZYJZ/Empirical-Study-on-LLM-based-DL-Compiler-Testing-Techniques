

import torch  # Importing PyTorch library
from torch import nn  # Importing neural network module from PyTorch library

class Model(nn.Module):
    def __init__(self):
        super().__init__()
 
        self._network = nn.Sequential(
            nn.Conv2d(in_channels=3, out_channels=8, kernel_size=1),  # Applying a pointwise convolution with the specified input channel dimension (in_channels) and output channel dimensions (out_channels). A kernel size of 1 is used to avoid losing any information.
            nn.BatchNorm2d(num_features=8),                          # Apply batch normalization for each channel.
            nn.ConvTranspose2d(                                     # Applying a pointwise transposed convolution with the specified input and output channels
                in_channels=8, out_channels=3, kernel_size=(16, 16)   # The first parameter (in_channels) is the number of the input channels
            ),
            nn.Softmax(dim=-2),                                   # Applying a softmax function over each channel (in_channels) of the tensor
            nn.Sigmoid()                                          # Applying sigmoid activation to the output of the transposed convolution
        )
 
    def forward(self, x1):  # For model execution
        return self._network(x1)


