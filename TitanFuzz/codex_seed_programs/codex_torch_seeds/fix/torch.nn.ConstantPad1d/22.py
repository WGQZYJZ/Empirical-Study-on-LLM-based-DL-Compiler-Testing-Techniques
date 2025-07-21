'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ConstantPad1d\ntorch.nn.ConstantPad1d(padding, value)\n'
import torch
from torch.nn import ConstantPad1d
input = torch.arange(1, 5, dtype=torch.float32).reshape(1, 1, 4)
print(input)
padding = (1, 2)
value = (- 1)
constant_pad1d = ConstantPad1d(padding, value)
output = constant_pad1d(input)
print(output)