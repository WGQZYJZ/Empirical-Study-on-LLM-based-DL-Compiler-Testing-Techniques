'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.irfft\ntorch.fft.irfft(input, n=None, dim=-1, norm=None, *, out=None)\n'
import torch
import torch
input = torch.randn(4, 4)
print('Input data:', input)
output = torch.fft.irfft(input, n=4, dim=(- 1), norm=None, out=None)
print('Output data:', output)