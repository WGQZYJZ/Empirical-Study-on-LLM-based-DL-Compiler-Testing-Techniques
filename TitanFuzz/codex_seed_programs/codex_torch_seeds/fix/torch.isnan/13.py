'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isnan\ntorch.isnan(input)\n'
import torch
x = torch.tensor([1, float('nan'), float('inf')])
y = torch.isnan(x)
print(y)