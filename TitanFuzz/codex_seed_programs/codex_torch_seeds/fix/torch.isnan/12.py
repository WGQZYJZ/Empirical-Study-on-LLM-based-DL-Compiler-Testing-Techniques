'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isnan\ntorch.isnan(input)\n'
import torch
x = torch.tensor([1, float('nan'), float('inf')])
print(x)
print(torch.isnan(x))
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isfinite\ntorch.isfinite(input)\n'
import torch
x = torch.tensor([1, float('nan'), float('inf')])
print(x)
print(torch.isfinite(x))
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isinf\ntorch.isinf(input)\n'
import torch
x = torch.tensor([1, float('nan'), float('inf')])
print(x)
print(torch.isinf(x))