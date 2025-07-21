'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.fftn\ntorch.fft.fftn(input, s=None, dim=None, norm=None, *, out=None)\n'
import torch
x = torch.randn(10, 10)
print(x)
fft_x = torch.fft.fftn(x)
print(fft_x)