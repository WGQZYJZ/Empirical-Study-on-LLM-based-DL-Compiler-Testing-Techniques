'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.rfft2\ntorch.fft.rfft2(input, s=None, dim=(-2, -1), norm=None, *, out=None)\n'
import torch
import torch.fft
input = torch.randn(2, 2, 3)
print('Input data: ', input)
print('\n\n')
print('FFT of input data: ', torch.fft.rfft2(input))