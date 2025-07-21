'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Mish\ntorch.nn.Mish(inplace=False)\n'
import torch
from torch.nn import Mish
x = torch.rand(10)
print('Input: ', x)
mish_activation = Mish()
y = mish_activation(x)
print('Output: ', y)