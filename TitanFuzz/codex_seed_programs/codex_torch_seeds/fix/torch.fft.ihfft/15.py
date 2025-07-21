'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.ihfft\ntorch.fft.ihfft(input, n=None, dim=-1, norm=None, *, out=None)\n'
import torch
import torch
input = torch.rand(32, 32)
output = torch.fft.ihfft(input, norm=None)
print(output)