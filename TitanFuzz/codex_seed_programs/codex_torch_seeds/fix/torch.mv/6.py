'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.mv\ntorch.mv(input, vec, *, out=None)\n'
import torch
A = torch.randn(4, 3)
v = torch.randn(3)
out = torch.mv(A, v)
print(out)