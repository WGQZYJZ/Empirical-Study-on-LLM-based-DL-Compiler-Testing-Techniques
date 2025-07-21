'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.index_select\ntorch.index_select(input, dim, index, *, out=None)\n'
import torch
x = torch.randn(3, 4)
print(x)
print(x.shape)
indices = torch.tensor([0, 2])
print(indices)
y = torch.index_select(x, dim=0, index=indices)
print(y)
print(y.shape)