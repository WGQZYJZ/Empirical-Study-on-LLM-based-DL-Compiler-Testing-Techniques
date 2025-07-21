'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.lstsq\ntorch.lstsq(input, A, *, out=None)\n'
import torch
import torch
input = torch.randn(3, 3, requires_grad=True)
A = torch.randn(3, 3)
torch.lstsq(input, A)