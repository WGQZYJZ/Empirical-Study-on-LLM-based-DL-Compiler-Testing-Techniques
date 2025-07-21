'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LeakyReLU\ntorch.nn.LeakyReLU(negative_slope=0.01, inplace=False)\n'
import torch
import torch.nn as nn
x = torch.randn(1, 10)
leaky_relu = nn.LeakyReLU(negative_slope=0.01, inplace=False)
y = leaky_relu(x)
print(x)
print(y)