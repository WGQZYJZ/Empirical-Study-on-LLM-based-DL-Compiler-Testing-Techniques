'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Hardshrink\ntorch.nn.Hardshrink(lambd=0.5)\n'
import torch
import torch.nn as nn
input_data = torch.randn(2, 3)
print('input_data: \n', input_data)
hardshrink = nn.Hardshrink(lambd=0.5)
output = hardshrink(input_data)
print('output: \n', output)