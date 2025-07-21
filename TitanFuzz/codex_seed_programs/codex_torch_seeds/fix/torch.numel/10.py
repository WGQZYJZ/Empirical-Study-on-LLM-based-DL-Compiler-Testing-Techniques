'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.numel\ntorch.numel(input)\n'
import torch
input = torch.randn(3, 2, 5)
print(input)
print(torch.numel(input))