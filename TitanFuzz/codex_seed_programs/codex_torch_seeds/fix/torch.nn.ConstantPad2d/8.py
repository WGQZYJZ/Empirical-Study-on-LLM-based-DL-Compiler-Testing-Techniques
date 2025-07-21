'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ConstantPad2d\ntorch.nn.ConstantPad2d(padding, value)\n'
import torch
import torch.nn as nn
input = torch.randn(1, 1, 3, 3)
padding = (1, 1, 1, 1)
value = 0
output = nn.ConstantPad2d(padding, value)(input)
print(output)