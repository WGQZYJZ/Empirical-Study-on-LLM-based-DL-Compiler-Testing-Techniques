'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.real\ntorch.real(input)\n'
import torch
a = torch.randn(1, 3)
b = torch.randn(1, 3)
c = torch.real(a)
print(c)
d = torch.real(b)
print(d)