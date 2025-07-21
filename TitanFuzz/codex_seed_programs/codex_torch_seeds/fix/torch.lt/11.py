'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.lt\ntorch.lt(input, other, *, out=None)\n'
import torch
x = torch.tensor([1, 2, 3])
y = torch.tensor([1, 2, 3])
z = torch.lt(x, y)
print('The result of torch.lt: {}'.format(z))