'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Hardsigmoid\ntorch.nn.Hardsigmoid(inplace=False)\n'
import torch
input = torch.randn(2, 3)
output = torch.nn.Hardsigmoid(input)
print('output:', output)