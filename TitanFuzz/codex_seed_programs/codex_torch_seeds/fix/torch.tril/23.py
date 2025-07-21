'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tril\ntorch.tril(input, diagonal=0, *, out=None)\n'
import torch
x = torch.randn(4, 4)
print('x: ', x)
y = torch.tril(x, diagonal=1)
print('y: ', y)