'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.asin\ntorch.asin(input, *, out=None)\n'
import torch
x = torch.rand(5, 3)
print(x)
y = torch.asin(x)
print(y)