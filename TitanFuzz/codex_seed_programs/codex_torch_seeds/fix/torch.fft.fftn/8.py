'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.fftn\ntorch.fft.fftn(input, s=None, dim=None, norm=None, *, out=None)\n'
import torch
input = torch.randn(1, 1, 4, 4)
torch.fft.fftn(input)