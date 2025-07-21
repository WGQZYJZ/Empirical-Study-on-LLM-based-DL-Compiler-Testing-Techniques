'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.dist\ntorch.dist(input, other, p=2)\n'
import torch
input = torch.randn(4, 3)
other = torch.randn(4, 3)
result = torch.dist(input, other, p=2)
print('result = ', result)