'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ConstantPad1d\ntorch.nn.ConstantPad1d(padding, value)\n'
import torch
from torch import nn
x = torch.ones(3, 2, 3)
print(x)
padding = (0, 1)
value = (- 1)
y = nn.ConstantPad1d(padding, value)(x)
print(y)