'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.histogram\ntorch.Tensor.histogram(_input_tensor, input, bins, *, range=None, weight=None, density=False)\n'
import torch
input_tensor = torch.randn(10)
hist = torch.Tensor.histogram(input_tensor, input_tensor, bins=10)
print('hist:', hist)