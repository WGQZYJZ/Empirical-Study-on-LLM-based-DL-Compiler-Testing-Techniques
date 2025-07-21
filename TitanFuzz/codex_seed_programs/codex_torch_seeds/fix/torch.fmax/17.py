'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fmax\ntorch.fmax(input, other, *, out=None)\n'
import torch
a = torch.rand(3, 3)
b = torch.rand(3, 3)
print(torch.fmax(a, b))
print(torch.fmax(a, b, out=torch.empty(3, 3)))
print(torch.fmax(a, b, out=torch.empty(3, 3).fill_(2)))