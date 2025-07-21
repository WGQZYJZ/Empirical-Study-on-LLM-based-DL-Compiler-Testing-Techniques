'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isnan\ntorch.isnan(input)\n'
import torch
x = torch.randn(1, 3)
y = torch.isnan(x)
print(x)
print(y)