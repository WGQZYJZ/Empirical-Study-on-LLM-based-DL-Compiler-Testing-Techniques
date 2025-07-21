'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.lstsq\ntorch.lstsq(input, A, *, out=None)\n'
import torch
import torch
A = torch.randn(3, 3)
b = torch.randn(3, 1)
x = torch.lstsq(b, A)
print('A:', A)
print('b:', b)
print('x:', x)