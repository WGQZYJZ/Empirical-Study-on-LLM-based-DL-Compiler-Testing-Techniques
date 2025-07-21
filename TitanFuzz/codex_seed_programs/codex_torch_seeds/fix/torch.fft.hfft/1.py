'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.hfft\ntorch.fft.hfft(input, n=None, dim=-1, norm=None, *, out=None)\n'
import torch
input = torch.randn(1, 2, 4, 2, dtype=torch.complex64)
output = torch.fft.hfft(input, n=None, dim=(- 1), norm=None)
print(input)
print(output)