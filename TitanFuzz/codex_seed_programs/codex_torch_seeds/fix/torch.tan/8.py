'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tan\ntorch.tan(input, *, out=None)\n'
import torch
input = torch.randn(4, 4)
print('Input data: {}'.format(input))
print('Output data: {}'.format(torch.tan(input)))