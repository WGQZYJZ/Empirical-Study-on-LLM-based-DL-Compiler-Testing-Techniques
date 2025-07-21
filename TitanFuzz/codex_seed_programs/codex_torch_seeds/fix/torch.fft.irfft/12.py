'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.irfft\ntorch.fft.irfft(input, n=None, dim=-1, norm=None, *, out=None)\n'
import torch
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
input = torch.randn(4, 8, 32)
print('Task 3: Call the API torch.fft.irfft')
output = torch.fft.irfft(input, n=None, dim=(- 1), norm=None, out=None)
print('input: ', input)
print('output: ', output)