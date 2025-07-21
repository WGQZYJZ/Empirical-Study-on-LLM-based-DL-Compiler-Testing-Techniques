'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.triu\ntorch.triu(input, diagonal=0, *, out=None)\n'
import torch
input = torch.randn(3, 3)
print(input)
result = torch.triu(input)
print(result)
result = torch.triu(input, diagonal=1)
print(result)
result = torch.triu(input, diagonal=(- 1))
print(result)