'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.rfft2\ntorch.fft.rfft2(input, s=None, dim=(-2, -1), norm=None, *, out=None)\n'
import torch
import torch
input = torch.randn(4, 4, dtype=torch.float)
print(input)
output = torch.fft.rfft2(input)
print(output)