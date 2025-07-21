'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ConstantPad3d\ntorch.nn.ConstantPad3d(padding, value)\n'
import torch
from torch.nn import ConstantPad3d
input = torch.randn(1, 1, 3, 3, 3)
padding = (1, 1, 1, 1, 1, 1)
value = 0
constant_padding = ConstantPad3d(padding, value)
output = constant_padding(input)
print(output)