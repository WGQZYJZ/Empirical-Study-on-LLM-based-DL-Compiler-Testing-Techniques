'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ConstantPad1d\ntorch.nn.ConstantPad1d(padding, value)\n'
import torch
import torch.nn as nn
input = torch.randn(1, 1, 4, requires_grad=True)
print('Input: ', input)
padding_size = 1
constant_pad = nn.ConstantPad1d(padding_size, 1)
output = constant_pad(input)
print('Output: ', output)