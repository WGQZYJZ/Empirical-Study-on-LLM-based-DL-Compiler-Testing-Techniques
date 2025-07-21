'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.less\ntorch.less(input, other, *, out=None)\n'
import torch
print('PyTorch version: ', torch.__version__)
x = torch.tensor([1, 2, 3, 4, 5])
y = torch.tensor([5, 4, 3, 2, 1])
print('x < y: ', torch.less(x, y))
print('x < y: ', torch.lt(x, y))
print('x < y: ', (x < y))
print('x < y: ', torch.less(x, 3))
print('x < y: ', torch.lt(x, 3))
print('x < y: ', (x < 3))