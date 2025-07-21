'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.sinc\ntorch.special.sinc(input, *, out=None)\n'
import torch
input = torch.randn(1, 1, 5)
print('Input data =\n', input)
output = torch.special.sinc(input)
print('Output data =\n', output)