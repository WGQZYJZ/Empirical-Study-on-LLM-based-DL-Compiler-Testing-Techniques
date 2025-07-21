'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.index_select\ntorch.index_select(input, dim, index, *, out=None)\n'
import torch
x = torch.randn(3, 4)
print('x:')
print(x)
print('x.size():')
print(x.size())
print('torch.index_select(x, 0, torch.tensor([0, 2])):')
print(torch.index_select(x, 0, torch.tensor([0, 2])))
print('torch.index_select(x, 1, torch.tensor([0, 2])):')
print(torch.index_select(x, 1, torch.tensor([0, 2])))
print('torch.index_select(x, 1, torch.tensor([0, 2])).size():')
print(torch.index_select(x, 1, torch.tensor([0, 2])).size())