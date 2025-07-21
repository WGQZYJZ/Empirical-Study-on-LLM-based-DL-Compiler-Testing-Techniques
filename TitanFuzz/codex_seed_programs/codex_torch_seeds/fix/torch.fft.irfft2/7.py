'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.irfft2\ntorch.fft.irfft2(input, s=None, dim=(-2, -1), norm=None, *, out=None)\n'
import torch
import torch.fft
import torch
import torch.fft
input = torch.randn(1, 2, 5, 5)
output = torch.fft.irfft2(input)
print(output)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.rfft\ntorch.fft.rfft(input, signal_ndim, normalized=False, onesided=True, *, out=None)\n'
import torch
import torch.fft
import torch
import torch.fft
input = torch.randn(1, 2, 5, 5)
output = torch.fft.rfft(input)
print(output)