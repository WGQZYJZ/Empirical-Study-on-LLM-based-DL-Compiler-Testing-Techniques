'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.rfftn\ntorch.fft.rfftn(input, s=None, dim=None, norm=None, *, out=None)\n'
import torch
a = torch.randn(4, 4, 4)
print(a)
b = torch.fft.rfftn(a)
print(b)