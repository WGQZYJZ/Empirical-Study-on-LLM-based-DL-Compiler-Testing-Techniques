'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Hardshrink\ntorch.nn.Hardshrink(lambd=0.5)\n'
import torch
import torch.nn as nn
input_data = torch.randn(4, 4)
hardshrink = nn.Hardshrink(lambd=0.5)
output = hardshrink(input_data)
print('Input: ', input_data)
print('Output: ', output)