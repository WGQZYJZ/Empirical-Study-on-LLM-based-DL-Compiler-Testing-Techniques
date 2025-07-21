'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.fftn\ntorch.fft.fftn(input, s=None, dim=None, norm=None, *, out=None)\n'
import torch
input = torch.randn(4, 5, 6, 7, 8)
output = torch.fft.fftn(input)
print(output.shape)