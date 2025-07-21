'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.RReLU\ntorch.nn.RReLU(lower=0.125, upper=0.3333333333333333, inplace=False)\n'
import torch
import torch.nn as nn
input = torch.randn(1, 1, 3, 3)
rrelu = nn.RReLU(lower=0.125, upper=0.3333333333333333, inplace=False)
output = rrelu(input)
print(output)
print(output)