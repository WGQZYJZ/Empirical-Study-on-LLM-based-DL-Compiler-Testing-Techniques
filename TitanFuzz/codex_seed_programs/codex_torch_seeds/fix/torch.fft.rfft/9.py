'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.rfft\ntorch.fft.rfft(input, n=None, dim=-1, norm=None, *, out=None)\n'
import torch
input = torch.randn(1, 10, 2)
output = torch.fft.rfft(input, n=None, dim=(- 1), norm=None, out=None)
print(output)