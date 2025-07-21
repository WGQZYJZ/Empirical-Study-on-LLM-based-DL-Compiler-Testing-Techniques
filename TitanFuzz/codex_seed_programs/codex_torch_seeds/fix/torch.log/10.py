'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.log\ntorch.log(input, *, out=None)\n'
import torch
x = torch.randn(2, 3)
print('Input data:\n{}'.format(x))
y = torch.log(x)
print('Output data:\n{}'.format(y))