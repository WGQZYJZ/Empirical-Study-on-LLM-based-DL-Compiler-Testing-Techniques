'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.rfft\ntorch.fft.rfft(input, n=None, dim=-1, norm=None, *, out=None)\n'
import torch
x = torch.randn(1, 2, 3, 4, 5)
y = torch.fft.rfft(x, n=None, dim=(- 1), norm=None, out=None)
print(y)