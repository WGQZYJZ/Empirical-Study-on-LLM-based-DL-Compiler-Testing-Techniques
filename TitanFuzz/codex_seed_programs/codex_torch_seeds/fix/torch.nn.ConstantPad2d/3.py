'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ConstantPad2d\ntorch.nn.ConstantPad2d(padding, value)\n'
import torch
import numpy as np
input = torch.ones(1, 1, 3, 3)
print('Input data: ', input)
padding_value = torch.nn.ConstantPad2d(padding=(1, 1, 1, 1), value=0)
output = padding_value(input)
print('Output data: ', output)