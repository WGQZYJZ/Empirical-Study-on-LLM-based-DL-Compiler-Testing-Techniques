'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.histogram\ntorch.histogram(input, bins, *, range=None, weight=None, density=False, out=None)\n'
import torch
input_data = torch.randn(10, 3)
hist = torch.histogram(input_data, bins=10, range=((- 1), 1))
print('hist: ', hist)
hist = torch.histogram(input_data, bins=10, range=((- 1), 1), density=True)
print('hist: ', hist)
hist = torch.histogram(input_data, bins=10, range=((- 1), 1), density=False)
print('hist: ', hist)