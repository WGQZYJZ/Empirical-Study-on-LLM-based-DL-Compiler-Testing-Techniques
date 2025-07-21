'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.lstsq\ntorch.lstsq(input, A, *, out=None)\n'
import torch
A = torch.randn(2, 3)
b = torch.randn(2)
x = torch.lstsq(b, A)
print(x)