'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ReLU\ntorch.nn.ReLU(inplace=False)\n'
import torch
import torch.nn as nn
input = torch.randn(1, 5, requires_grad=True)
output = nn.ReLU(inplace=False)(input)
print('input', input)
print('output', output)