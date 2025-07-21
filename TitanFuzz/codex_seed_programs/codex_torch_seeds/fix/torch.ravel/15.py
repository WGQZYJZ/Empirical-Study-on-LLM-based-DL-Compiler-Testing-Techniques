'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.ravel\ntorch.ravel(input)\n'
import torch
x = torch.randn(4, 4)
print(x)
print(torch.ravel(x))