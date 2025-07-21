'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.ravel\ntorch.ravel(input)\n'
import torch
input = torch.randn(1, 2, 3, 4)
print(input)
output = torch.ravel(input)
print(output)