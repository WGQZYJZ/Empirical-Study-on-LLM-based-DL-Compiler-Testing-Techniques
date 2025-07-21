'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.rfft\ntorch.fft.rfft(input, n=None, dim=-1, norm=None, *, out=None)\n'
import torch
import torch.fft
input = torch.randn(2, 3, 4)
output = torch.fft.rfft(input)
print(output)