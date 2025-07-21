'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.histc\ntorch.histc(input, bins=100, min=0, max=0, *, out=None)\n'
import torch
import torch
input_data = torch.randn(1000)
hist_data = torch.histc(input_data, bins=100, min=0, max=0)
print('hist_data: ', hist_data)