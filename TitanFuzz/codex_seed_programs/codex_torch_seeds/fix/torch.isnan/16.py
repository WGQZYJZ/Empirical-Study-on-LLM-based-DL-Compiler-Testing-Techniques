'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isnan\ntorch.isnan(input)\n'
import torch
input = torch.randn(1, 3)
input[(0, 0)] = float('nan')
input[(0, 2)] = float('inf')
print(torch.isnan(input))