'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isfinite\ntorch.isfinite(input)\n'
import torch
a = torch.Tensor([1, 2, 3, float('nan')])
b = torch.Tensor([1, float('inf'), float('-inf'), float('nan')])
print(torch.isfinite(a))
print(torch.isfinite(b))