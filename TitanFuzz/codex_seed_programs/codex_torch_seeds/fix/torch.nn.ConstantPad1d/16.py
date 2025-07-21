'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ConstantPad1d\ntorch.nn.ConstantPad1d(padding, value)\n'
import torch
import torch.nn as nn
x = torch.tensor([[1, 2, 3, 4, 5]])
print('Input data: {}'.format(x))
pad = nn.ConstantPad1d((2, 3), value=0)
print('Output data: {}'.format(pad(x)))