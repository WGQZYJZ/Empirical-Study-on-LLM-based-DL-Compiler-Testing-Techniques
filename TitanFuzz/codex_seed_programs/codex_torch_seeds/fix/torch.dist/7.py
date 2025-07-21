'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.dist\ntorch.dist(input, other, p=2)\n'
import torch
input = torch.randn(3, 5, requires_grad=True)
other = torch.randn(3, 5)
result = torch.dist(input, other, p=2)
print(result)
result = torch.dist(input, other, p=1)
print(result)