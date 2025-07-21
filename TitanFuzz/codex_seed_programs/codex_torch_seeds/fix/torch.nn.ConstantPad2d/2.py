'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ConstantPad2d\ntorch.nn.ConstantPad2d(padding, value)\n'
import torch
from torch.nn import ConstantPad2d
input = torch.tensor([[[[1, 2, 3], [4, 5, 6], [7, 8, 9]]]])
constant_pad = ConstantPad2d(padding=2, value=0)
output = constant_pad(input)
print(output)