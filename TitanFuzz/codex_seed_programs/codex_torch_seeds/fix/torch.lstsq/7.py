'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.lstsq\ntorch.lstsq(input, A, *, out=None)\n'
import torch
import torch
A = torch.randn(3, 2)
b = torch.randn(3)
(x, _) = torch.lstsq(b, A)
print(x)