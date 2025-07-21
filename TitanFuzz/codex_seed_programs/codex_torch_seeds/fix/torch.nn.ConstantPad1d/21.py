'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ConstantPad1d\ntorch.nn.ConstantPad1d(padding, value)\n'
import torch
from torch import nn
from torch.nn import functional as F
import torch
from torch import nn
from torch.nn import functional as F
input = torch.arange(0, 6).reshape(1, 1, 6)
print(input)
padding = (1, 1)
value = 0
layer = nn.ConstantPad1d(padding, value)
output = layer(input)
print(output)