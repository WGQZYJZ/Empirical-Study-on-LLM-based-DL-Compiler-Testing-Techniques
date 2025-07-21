'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ConstantPad3d\ntorch.nn.ConstantPad3d(padding, value)\n'
import torch
import torch.nn as nn
input_tensor = torch.randn(1, 3, 3, 3, 3)
padding = (1, 1, 1, 1, 1, 1)
value = 0
constant_pad3d = nn.ConstantPad3d(padding, value)
output_tensor = constant_pad3d(input_tensor)
print('input_tensor: ', input_tensor)
print('output_tensor: ', output_tensor)