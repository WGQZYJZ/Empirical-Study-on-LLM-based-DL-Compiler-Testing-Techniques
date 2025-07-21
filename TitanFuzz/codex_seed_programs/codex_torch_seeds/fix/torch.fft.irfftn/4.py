'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.irfftn\ntorch.fft.irfftn(input, s=None, dim=None, norm=None, *, out=None)\n'
import torch
import torch
input = torch.randn(2, 3, 4, 5, 6)
torch.fft.irfftn(input, s=None, dim=None, norm=None, out=None)