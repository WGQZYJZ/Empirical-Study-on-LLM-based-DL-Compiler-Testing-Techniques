'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.fftn\ntorch.fft.fftn(input, s=None, dim=None, norm=None, *, out=None)\n'
import torch
import torch.fft
input = torch.randn(4, 4)
print('Input data: \n', input)
output = torch.fft.fftn(input, dim=0)
print('Output data: \n', output)