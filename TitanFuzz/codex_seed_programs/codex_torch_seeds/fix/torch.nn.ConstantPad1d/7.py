'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ConstantPad1d\ntorch.nn.ConstantPad1d(padding, value)\n'
import torch
from torch.nn import ConstantPad1d
input = torch.tensor([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
print('Input data: \n', input)
padding = 2
value = 0
constant_pad1d = ConstantPad1d(padding, value)
output = constant_pad1d(input)
print('\nOutput data: \n', output)