'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.diag\ntorch.diag(input, diagonal=0, *, out=None)\n'
import torch
input = torch.randn(5, 5)
print(input)
print(torch.diag(input))
print(torch.diag(input, diagonal=1))
print(torch.diag(input, diagonal=(- 1)))
print(torch.diag(input, diagonal=2))