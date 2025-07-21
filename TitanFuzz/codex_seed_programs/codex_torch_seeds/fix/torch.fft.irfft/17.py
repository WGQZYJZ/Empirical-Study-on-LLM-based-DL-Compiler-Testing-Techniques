'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.irfft\ntorch.fft.irfft(input, n=None, dim=-1, norm=None, *, out=None)\n'
import torch
input = torch.randn(1, 1, 4, 4)
output = torch.fft.irfft(input)
print(output)