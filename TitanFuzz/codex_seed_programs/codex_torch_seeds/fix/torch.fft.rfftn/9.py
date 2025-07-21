'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.rfftn\ntorch.fft.rfftn(input, s=None, dim=None, norm=None, *, out=None)\n'
import torch
x = torch.randn(1, 2, 3, 4, 5)
print(x.shape)
y = torch.fft.rfftn(x, 3)
print(y.shape)
z = torch.fft.irfftn(y, 3)
print(z.shape)
print(z)
print(x)