'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isfinite\ntorch.isfinite(input)\n'
import torch
x = torch.tensor([1, 2, float('inf'), float('nan')])
y = torch.isfinite(x)
print(y)
'\nOutput:\ntensor([1, 1, 0, 0])\n'