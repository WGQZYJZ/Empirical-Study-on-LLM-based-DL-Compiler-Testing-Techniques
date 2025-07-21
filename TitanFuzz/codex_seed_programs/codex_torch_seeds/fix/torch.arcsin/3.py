'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.arcsin\ntorch.arcsin(input, *, out=None)\n'
import torch
input_data = torch.randn(3, 3)
print('Input data: ', input_data)
torch_arcsin = torch.arcsin(input_data)
print('Result of torch.arcsin: ', torch_arcsin)