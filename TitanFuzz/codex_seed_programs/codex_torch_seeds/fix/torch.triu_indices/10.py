"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.triu_indices\ntorch.triu_indices(row, col, offset=0, *, dtype=torch.long, device='cpu', layout=torch.strided)\n"
import torch
a = torch.rand(2, 3, 4)
print(torch.triu_indices(row=2, col=3))
print(torch.triu_indices(row=2, col=3, offset=1))
print(torch.triu_indices(row=2, col=3, offset=2))