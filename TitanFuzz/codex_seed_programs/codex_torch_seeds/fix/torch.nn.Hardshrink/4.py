'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Hardshrink\ntorch.nn.Hardshrink(lambd=0.5)\n'
import torch
import torch.nn as nn
input_data = torch.randn(1, 3, 3, 3)
print('Input data: ', input_data)
hardshrink_layer = nn.Hardshrink(lambd=0.5)
output = hardshrink_layer(input_data)
print('Output: ', output)