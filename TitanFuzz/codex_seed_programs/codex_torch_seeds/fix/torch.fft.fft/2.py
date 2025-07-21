'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.fft\ntorch.fft.fft(input, n=None, dim=-1, norm=None, *, out=None)\n'
import torch
input = torch.randn(1, 4, 5)
output = torch.fft.fft(input)
print(output)
print(output.shape)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.ifft\ntorch.fft.ifft(input, n=None, dim=-1, norm=None, *, out=None)\n'
import torch
input = torch.randn(1, 4, 5)
output = torch.fft.ifft(input)
print(output)
print(output.shape)