'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isfinite\ntorch.isfinite(input)\n'
import torch
x = torch.randn(2, 3)
print(x)
y = torch.isfinite(x)
print(y)