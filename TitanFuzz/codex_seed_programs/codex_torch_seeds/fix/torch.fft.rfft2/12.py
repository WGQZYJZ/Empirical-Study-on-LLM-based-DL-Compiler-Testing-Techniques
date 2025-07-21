'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.rfft2\ntorch.fft.rfft2(input, s=None, dim=(-2, -1), norm=None, *, out=None)\n'
import torch
inp = torch.randn(2, 3, 4, 5)
out = torch.fft.rfft2(inp)
print(out.size())