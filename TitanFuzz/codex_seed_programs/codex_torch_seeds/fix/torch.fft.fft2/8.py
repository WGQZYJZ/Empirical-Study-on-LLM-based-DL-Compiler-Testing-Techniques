'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.fft2\ntorch.fft.fft2(input, s=None, dim=(-2, -1), norm=None, *, out=None)\n'
import torch
input = torch.rand(10, 10)
output = torch.fft.fft2(input)
print('Input: {}'.format(input))
print('Output: {}'.format(output))