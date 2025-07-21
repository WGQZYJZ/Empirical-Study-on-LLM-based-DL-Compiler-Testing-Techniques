'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ConstantPad2d\ntorch.nn.ConstantPad2d(padding, value)\n'
import torch
import torch.nn as nn
input = torch.randn(1, 1, 4, 4)
print('Input data: \n', input)
padding = (1, 1, 1, 1)
value = 0
constant_padding = nn.ConstantPad2d(padding, value)
output = constant_padding(input)
print('Output data: \n', output)