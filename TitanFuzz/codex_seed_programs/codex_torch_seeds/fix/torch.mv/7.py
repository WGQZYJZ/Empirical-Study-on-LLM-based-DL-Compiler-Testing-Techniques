'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.mv\ntorch.mv(input, vec, *, out=None)\n'
import torch
input = torch.rand(3, 4, dtype=torch.float32)
vec = torch.rand(4, dtype=torch.float32)
torch.mv(input, vec)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.mm\ntorch.mm(input, mat2, *, out=None)\n'
import torch
input = torch.rand(3, 4, dtype=torch.float32)
mat2 = torch.rand(4, 5, dtype=torch.float32)
torch.mm(input, mat2)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bmm\ntorch.bmm(input, mat2, *, out=None)\n'
import torch