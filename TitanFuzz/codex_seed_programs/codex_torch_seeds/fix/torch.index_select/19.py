'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.index_select\ntorch.index_select(input, dim, index, *, out=None)\n'
import torch
import torch
input = torch.randn(3, 4)
index = torch.tensor([0, 2])
output = torch.index_select(input, 0, index)
print(output)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.index_select\ntorch.index_select(input, dim, index, *, out=None)\n'
import torch
import torch
input = torch.randn(3, 4)
index = torch.tensor([0, 2])
output = torch.index_select(input, 1, index)
print(output)