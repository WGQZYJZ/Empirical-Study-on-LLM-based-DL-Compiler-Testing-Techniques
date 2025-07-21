'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.mm\ntorch.mm(input, mat2, *, out=None)\n'
import torch
import torch
input = torch.tensor([[1, 2, 3], [4, 5, 6]])
mat2 = torch.tensor([[1, 2], [3, 4], [5, 6]])
torch.mm(input, mat2)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bmm\ntorch.bmm(input, mat2, *, out=None)\n'
import torch
import torch
input = torch.randn(10, 3, 4)
mat2 = torch.randn(10, 4, 5)
torch.bmm(input, mat2)