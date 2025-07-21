'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.mv\ntorch.mv(input, vec, *, out=None)\n'
import torch
import torch
input = torch.randn(2, 3)
vec = torch.randn(3)
torch.mv(input, vec)
out = torch.randn(2)
torch.mv(input, vec, out=out)
torch.mm(input, vec.view(3, 1))
out = torch.randn(2, 1)
torch.mm(input, vec.view(3, 1), out=out)