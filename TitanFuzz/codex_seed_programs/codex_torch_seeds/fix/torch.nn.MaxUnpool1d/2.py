'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.MaxUnpool1d\ntorch.nn.MaxUnpool1d(kernel_size, stride=None, padding=0)\n'
import torch
import torch.nn as nn
import numpy as np
input = torch.Tensor(np.random.random((1, 3, 8)))
print('The input data:\n', input)
maxpool_layer = nn.MaxPool1d(kernel_size=2, stride=2, return_indices=True)
(output, indices) = maxpool_layer(input)
print('The output of the maxpool layer:\n', output)
print('The indices of the maxpool layer:\n', indices)
maxunpool_layer = nn.MaxUnpool1d(kernel_size=2, stride=2)
unpool_output = maxunpool_layer(output, indices)
print('The output of the maxunpool layer:\n', unpool_output)