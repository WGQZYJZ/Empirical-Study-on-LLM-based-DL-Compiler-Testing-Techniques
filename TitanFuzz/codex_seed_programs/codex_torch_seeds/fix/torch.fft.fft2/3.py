'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.fft2\ntorch.fft.fft2(input, s=None, dim=(-2, -1), norm=None, *, out=None)\n'
import torch
import torch.nn.functional as F
input = torch.randn(1, 1, 8, 8, requires_grad=True)
output = torch.fft.fft2(input)
print(input)
print(output)