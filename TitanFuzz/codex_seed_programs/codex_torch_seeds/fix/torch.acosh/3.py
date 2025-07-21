'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.acosh\ntorch.acosh(input, *, out=None)\n'
import torch
data = torch.randn(5)
print(data)
print(('-' * 20))
print(torch.acosh(data))