'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isinf\ntorch.isinf(input)\n'
import torch
import torch
input = torch.randn(2, 3, 4)
torch.isinf(input)
print(torch.isinf(input))
print(torch.isinf(input).any())
print(torch.isinf(input).all())
print(torch.isinf(input).sum())
print(torch.isinf(input).prod())
print(torch.isinf(input).dim())
print(torch.isinf(input).shape)
print(torch.isinf(input).size())