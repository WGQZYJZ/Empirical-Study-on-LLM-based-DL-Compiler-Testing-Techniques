'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.irfft\ntorch.fft.irfft(input, n=None, dim=-1, norm=None, *, out=None)\n'
import torch
import torch.nn.functional as F
input = torch.randn(1, 2, 3)
print(input)
output = torch.fft.irfft(input, n=None, dim=(- 1), norm=None, out=None)
print(output)