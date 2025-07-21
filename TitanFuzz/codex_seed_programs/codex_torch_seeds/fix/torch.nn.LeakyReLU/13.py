'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LeakyReLU\ntorch.nn.LeakyReLU(negative_slope=0.01, inplace=False)\n'
import torch
from torch.nn import LeakyReLU
input = torch.randn(1, 1, 3, 3)
print(input)
leaky_relu = LeakyReLU(negative_slope=0.01, inplace=False)
output = leaky_relu(input)
print(output)