'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.lstsq\ntorch.lstsq(input, A, *, out=None)\n'
import torch
input = torch.randn(10, 20, requires_grad=True)
A = torch.randn(10, 10)
torch.lstsq(input, A)