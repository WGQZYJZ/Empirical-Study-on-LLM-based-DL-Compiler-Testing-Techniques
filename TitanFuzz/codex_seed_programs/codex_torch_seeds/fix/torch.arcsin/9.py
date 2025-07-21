'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.arcsin\ntorch.arcsin(input, *, out=None)\n'
import torch
data = torch.randn(1, 3, 4, 5)
print('Input data:\n', data)
arcsin_data = torch.arcsin(data)
print('\narcsin_data:\n', arcsin_data)