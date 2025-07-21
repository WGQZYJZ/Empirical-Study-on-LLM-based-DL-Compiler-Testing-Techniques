'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.neg\ntorch.neg(input, *, out=None)\n'
import torch
x = torch.randn(1, 3)
print('Input data: \n', x)
print('Negative of input data: \n', torch.neg(x))