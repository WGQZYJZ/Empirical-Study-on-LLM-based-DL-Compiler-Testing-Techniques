'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.irfftn\ntorch.fft.irfftn(input, s=None, dim=None, norm=None, *, out=None)\n'
import torch
N = 16
x = torch.randn(N, N, N)
y = torch.fft.irfftn(x)
print(y)