'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ConstantPad2d\ntorch.nn.ConstantPad2d(padding, value)\n'
import torch
from torch.nn import ConstantPad2d
input = torch.ones(1, 1, 3, 3)
constant_pad = ConstantPad2d(padding=(1, 1, 1, 1), value=0)
output = constant_pad(input)
print(output)