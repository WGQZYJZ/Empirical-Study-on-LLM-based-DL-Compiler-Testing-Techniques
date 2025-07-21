'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.ifft2\ntorch.fft.ifft2(input, s=None, dim=(-2, -1), norm=None, *, out=None)\n'
import torch
import torch.fft
input = torch.randn(1, 2, 3, 4, 5)
output = torch.fft.ifft2(input)
print(output)