'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LeakyReLU\ntorch.nn.LeakyReLU(negative_slope=0.01, inplace=False)\n'
import torch
from torch.nn import LeakyReLU
x = torch.randn(2, 2)
print('Input data: ', x)
leaky_relu = LeakyReLU(negative_slope=0.01, inplace=False)
y = leaky_relu(x)
print('Output data: ', y)