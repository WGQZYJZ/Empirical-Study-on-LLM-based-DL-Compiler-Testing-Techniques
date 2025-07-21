'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.triu\ntorch.triu(input, diagonal=0, *, out=None)\n'
import torch
x = torch.randn(3, 3)
print(x)
print(torch.triu(x))
print(torch.triu(x, diagonal=1))
print(torch.triu(x, diagonal=(- 1)))