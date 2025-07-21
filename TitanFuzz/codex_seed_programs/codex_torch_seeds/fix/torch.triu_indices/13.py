"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.triu_indices\ntorch.triu_indices(row, col, offset=0, *, dtype=torch.long, device='cpu', layout=torch.strided)\n"
import torch
row = 5
col = 5
indices = torch.triu_indices(row, col, offset=0, dtype=torch.long)
print('indices = ', indices)
print('indices.shape = ', indices.shape)
print('indices.dtype = ', indices.dtype)