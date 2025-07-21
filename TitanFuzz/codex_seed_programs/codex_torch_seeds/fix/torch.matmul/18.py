'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.matmul\ntorch.matmul(input, other, *, out=None)\n'
import torch
input = torch.randn(3, 4)
other = torch.randn(4, 5)
torch.matmul(input, other)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.mm\ntorch.mm(input, other)\n'
import torch
input = torch.randn(3, 4)
other = torch.randn(4, 5)
torch.mm(input, other)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.mv\ntorch.mv(input, vec)\n'
import torch
input = torch.randn(3, 4)
vec = torch.randn(4)
torch.mv(input, vec)