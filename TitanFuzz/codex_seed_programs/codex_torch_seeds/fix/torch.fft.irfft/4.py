'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.irfft\ntorch.fft.irfft(input, n=None, dim=-1, norm=None, *, out=None)\n'
import torch
import torch.fft
input = torch.rand(2, 3, 4, 5)
output = torch.fft.irfft(input, n=None, dim=(- 1), norm=None, out=None)
print(output)