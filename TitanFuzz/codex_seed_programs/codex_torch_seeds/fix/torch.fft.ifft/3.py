'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.ifft\ntorch.fft.ifft(input, n=None, dim=-1, norm=None, *, out=None)\n'
import torch
input = torch.randn(2, 4, 5)
output = torch.fft.ifft(input, norm=None)
print(output)