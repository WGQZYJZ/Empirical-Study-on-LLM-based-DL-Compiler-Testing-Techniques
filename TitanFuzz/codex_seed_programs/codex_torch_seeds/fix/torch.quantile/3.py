'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.quantile\ntorch.quantile(input, q, dim=None, keepdim=False, *, out=None)\n'
import torch
import torch
input_data = torch.rand(10, 3)
torch.quantile(input_data, 0.5, dim=1, keepdim=True)