"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.triu_indices\ntorch.triu_indices(row, col, offset=0, *, dtype=torch.long, device='cpu', layout=torch.strided)\n"
import torch
x = torch.rand(3, 3)
print('Input data: ', x)
indices = torch.triu_indices(3, 3, offset=0, dtype=torch.long)
print('Indices: ', indices)
print('Result: ', x[(indices[0], indices[1])])