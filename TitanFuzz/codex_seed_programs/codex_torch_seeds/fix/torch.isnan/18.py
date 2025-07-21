'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isnan\ntorch.isnan(input)\n'
import torch
a = torch.tensor([1, 2, 3, float('nan')])
print(torch.isnan(a))
b = torch.tensor([1, 2, 3, float('inf')])
print(torch.isinf(b))