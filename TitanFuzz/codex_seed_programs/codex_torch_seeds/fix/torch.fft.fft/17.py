'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.fft\ntorch.fft.fft(input, n=None, dim=-1, norm=None, *, out=None)\n'
import torch
import torch.fft
input = torch.randn(4, 8)
output = torch.fft.fft(input, n=None, dim=(- 1), norm=None, out=None)
print(output)