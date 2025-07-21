'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ConstantPad2d\ntorch.nn.ConstantPad2d(padding, value)\n'
import torch
import torch.nn as nn
import torch
import torch.nn as nn
input = torch.randn(1, 3, 4, 4)
print(input)
pad = nn.ConstantPad2d(2, 0)
output = pad(input)
print(output)