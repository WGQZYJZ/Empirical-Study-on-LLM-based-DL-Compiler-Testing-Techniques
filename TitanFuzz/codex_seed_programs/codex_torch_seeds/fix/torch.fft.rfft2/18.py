'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.rfft2\ntorch.fft.rfft2(input, s=None, dim=(-2, -1), norm=None, *, out=None)\n'
import torch
input = torch.randn(2, 3, 4, 5)
print('Input:', input)
output = torch.fft.rfft2(input)
print('Output:', output)
'\nTask 4: Call the API torch.fft.irfft2\ntorch.fft.irfft2(input, s=None, dim=(-2, -1), norm=None, *, out=None)\n'
input = torch.randn(2, 3, 4, 5)
print('Input:', input)
output = torch.fft.irfft2(input)
print('Output:', output)