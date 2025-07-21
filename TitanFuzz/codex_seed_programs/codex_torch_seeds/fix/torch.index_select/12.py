'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.index_select\ntorch.index_select(input, dim, index, *, out=None)\n'
import torch
import torch
x = torch.randn(3, 4)
print('Input data: ', x)
indices = torch.tensor([0, 2])
print('Selected indices: ', indices)
y = torch.index_select(x, dim=0, index=indices)
print('Output data: ', y)
z = torch.zeros(2, 4)
torch.index_select(x, dim=0, index=indices, out=z)
print('Output data: ', z)