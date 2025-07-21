'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.fftn\ntorch.fft.fftn(input, s=None, dim=None, norm=None, *, out=None)\n'
import torch
import torch.fft
input = torch.randn(1, 2, 3, 4, 5)
torch.fft.fftn(input)
torch.fft.ifftn(input)