'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.triu\ntorch.triu(input, diagonal=0, *, out=None)\n'
import torch
input = torch.rand(3, 3)
print(input)
print(torch.triu(input))
print(torch.triu(input, diagonal=1))
print(torch.triu(input, diagonal=(- 1)))