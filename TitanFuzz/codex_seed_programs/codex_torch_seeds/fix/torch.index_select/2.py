'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.index_select\ntorch.index_select(input, dim, index, *, out=None)\n'
import torch
x = torch.randn(3, 4)
print('x: ', x)
y = torch.index_select(x, 0, torch.LongTensor([0, 2]))
print('y: ', y)