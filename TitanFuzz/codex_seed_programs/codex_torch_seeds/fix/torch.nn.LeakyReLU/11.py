'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LeakyReLU\ntorch.nn.LeakyReLU(negative_slope=0.01, inplace=False)\n'
import torch
import torch.nn as nn
input = torch.randn(2, 3)
leaky_relu = nn.LeakyReLU(0.01)
output = leaky_relu(input)
print(output)