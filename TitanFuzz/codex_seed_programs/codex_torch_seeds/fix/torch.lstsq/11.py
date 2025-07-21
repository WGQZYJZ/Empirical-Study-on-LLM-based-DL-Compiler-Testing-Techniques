'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.lstsq\ntorch.lstsq(input, A, *, out=None)\n'
import torch
print(torch.__version__)
A = torch.rand(3, 3)
b = torch.rand(3, 1)
x = torch.lstsq(b, A)
print(x)