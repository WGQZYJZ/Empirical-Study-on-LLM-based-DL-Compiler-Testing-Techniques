'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.numel\ntorch.numel(input)\n'
import torch
x = torch.randn(4, 4)
print(x)
print(torch.numel(x))