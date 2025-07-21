'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ConstantPad1d\ntorch.nn.ConstantPad1d(padding, value)\n'
import torch
from torch.nn import ConstantPad1d
input = torch.arange(1, 5, dtype=torch.float32)
print('Input: ', input)
padding = 2
value = 0
pad1d = ConstantPad1d(padding, value)
output = pad1d(input.view(1, 1, (- 1)))
print('Output: ', output)