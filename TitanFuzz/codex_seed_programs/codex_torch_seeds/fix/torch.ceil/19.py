'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.ceil\ntorch.ceil(input, *, out=None)\n'
import torch
input_data = torch.randn(1, 2, 3)
print('Input data: ', input_data)
torch.ceil(input_data)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.clamp\ntorch.clamp(input, min, max, *, out=None)\n'
import torch
input_data = torch.randn(1, 2, 3)
print('Input data: ', input_data)
torch.clamp(input_data, min=0.5, max=1.5)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.clamp_max\ntorch.clamp_max(input, max, *, out=None)\n'
import torch
input_data = torch.randn(1, 2, 3)
print('Input data: ', input_data)