'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Mish\ntorch.nn.Mish(inplace=False)\n'
import torch
from torch.nn import Mish
x = torch.randn(3, 3)
print('Input Data: ')
print(x)
mish = Mish()
out = mish(x)
print('Output Data: ')
print(out)