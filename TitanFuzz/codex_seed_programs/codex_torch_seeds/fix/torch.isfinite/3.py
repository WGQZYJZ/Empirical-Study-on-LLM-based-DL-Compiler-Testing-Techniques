'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isfinite\ntorch.isfinite(input)\n'
import torch
input = torch.randn(2, 3)
print(input)
print(torch.isfinite(input))
input = torch.randn(2, 3)
input[(0, 0)] = float('nan')
input[(1, 0)] = float('inf')
print(input)
print(torch.isfinite(input))