'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ReLU6\ntorch.nn.ReLU6(inplace=False)\n'
import torch
input = torch.randn(1, 3, 3, 3)
out = torch.nn.ReLU6(inplace=False)(input)
print('input:', input)
print('out:', out)