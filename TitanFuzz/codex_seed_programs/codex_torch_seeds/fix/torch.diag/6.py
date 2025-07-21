'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.diag\ntorch.diag(input, diagonal=0, *, out=None)\n'
import torch
data = torch.randn(3, 3)
print(data)
print(torch.diag(data))
print(torch.diag(data, diagonal=1))
print(torch.diag(data, diagonal=(- 1)))