'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.det\ntorch.det(input)\n'
import torch
input = torch.randn(2, 2)
print(input)
output = torch.det(input)
print(output)